# SPDX-FileCopyrightText: Copyright (c) 2023 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import sys
import os
import random
sys.path.append("/home/john/Projects/usd_scene_construction_utils") # use your install path

from usd_scene_construction_utils import *

# set to your output dir
OUTPUT_DIR = "/home/john/Projects/usd_scene_construction_utils/examples/replicator/output"


def add_box_stack(stage, path: str, box_material):
    container = add_xform(stage, path)
    boxes = []
    for i in range(3):
        box_path = f"{path}/box_{i}"
        box = add_box(stage, box_path, (random.uniform(20, 30), random.uniform(20, 30), 10))
        add_semantics(box, "class", "box_stack")
        bind_material(box, box_material)
        rotate_z(box, random.uniform(-10, 10))
        boxes.append(box)
    stack_prims(boxes, axis=2)
    return container


def build_scene(stage):
    # Add cardboard material
    cardboard = add_mdl_material(
        stage,
        "/scene/cardboard",
        "omniverse://ov-content/Library/Materials/Base/Wall_Board/Cardboard.mdl"
    )

    # Add concrete material
    concrete = add_mdl_material(
        stage,
        "/scene/concrete",
        "omniverse://ov-content/Library/Materials/Base/Masonry/Concrete_Smooth.mdl"
    )

    # Add floor plane
    floor = add_plane(stage, "/scene/floor", size=(500, 500))
    bind_material(floor, concrete)

    # Add box
    box_stack = add_box_stack(stage, "/scene/box_stack", box_material=cardboard)

    # Stack box on floor
    stack_prims([floor, box_stack], axis=2)

    # Add dome light
    add_dome_light(stage, "/scene/dome_light")


import omni.replicator.core as rep

with rep.new_layer():

    stage = new_omniverse_stage()
    build_scene(stage)

    camera = rep.create.camera()
    render_product = rep.create.render_product(camera, (1024, 1024))

    box_stack = rep.get.prims(path_pattern="^/scene/box_stack$")

    # Setup randomization
    with rep.trigger.on_frame(num_frames=100):
        with box_stack:
            rep.modify.pose(position=rep.distribution.uniform((-100, -100, 0), (100, 100, 0)))
        with camera:
            rep.modify.pose(position=rep.distribution.uniform((0, 0, 0), (400, 400, 400)), look_at=(0, 0, 0))

    writer = rep.WriterRegistry.get("BasicWriter")

    writer.initialize(
        output_dir=OUTPUT_DIR, 
        rgb=True,   
        bounding_box_2d_tight=True,
        distance_to_camera=True,
        bounding_box_3d=True,
        camera_params=True,
        instance_id_segmentation=True,
        colorize_instance_id_segmentation=False
    )

    writer.attach([render_product])