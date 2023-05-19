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
sys.path.append("/home/john/Projects/usd_scene_construction_utils")
from usd_scene_construction_utils import (
    add_usd_ref,
    rotate_x,
    rotate_y,
    rotate_z,
    scale,
    compute_bbox,
    add_xform,
    compute_bbox_center,
    translate,
    set_visibility,
    new_omniverse_stage,
    add_dome_light,
    add_plane,
    add_mdl_material,
    bind_material
)
import random
from typing import Tuple

box_asset_url = "omniverse://ov-content/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Shipping/Cardboard_Boxes/Flat_A//FlatBox_A02_15x21x8cm_PR_NVD_01.usd"
hand_truck_asset_url = "omniverse://ov-content/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Equipment/Hand_Trucks/Convertible_Aluminum_A/ConvertableAlumHandTruck_A02_PR_NVD_01.usd"


def add_box_of_size(
        stage,
        path: str, 
        size: Tuple[float, float, float]
    ):
    """Adds a box and re-scales it to match the specified dimensions
    """

    # Add USD box
    prim = add_usd_ref(stage, path, usd_path=box_asset_url)

    rotate_x(prim, random.choice([-90, 0, 90, 180]))
    rotate_y(prim, random.choice([-90, 0, 90, 180]))

    # Scale USD box to fit dimensions
    usd_min, usd_max = compute_bbox(prim)
    
    usd_size = (
        usd_max[0] - usd_min[0],
        usd_max[1] - usd_min[1],
        usd_max[2] - usd_min[2]
    )

    required_scale = (
        size[0] / usd_size[0],
        size[1] / usd_size[1],
        size[2] / usd_size[2]
    )

    scale(prim, required_scale)
    return prim


def add_random_box_stack(
        stage,
        path: str, 
        count_range=(1, 5),
        size_range=((30, 30, 10), (50, 50, 25)),
        angle_range=(-5, 5),
        jitter_range=(-3,3)
    ):
    container = add_xform(stage, path)
    count = random.randint(*count_range)

    # get sizes and sort
    sizes = [
        (
            random.uniform(size_range[0][0], size_range[1][0]),
            random.uniform(size_range[0][1], size_range[1][1]),
            random.uniform(size_range[0][2], size_range[1][2])
        )
        for i in range(count)
    ]

    sizes = sorted(sizes, key=lambda x: x[0]**2 + x[1]**2, reverse=True)

    boxes = []
    for i in range(count):
        box_i = add_box_of_size(stage, os.path.join(path, f"box_{i}"), sizes[i])
        boxes.append(box_i)

    if count > 0:
        center = compute_bbox_center(boxes[0])
        for i in range(1, count):
            prev_box, cur_box = boxes[i - 1], boxes[i]
            cur_bbox = compute_bbox(cur_box)
            cur_center = compute_bbox_center(cur_box)
            prev_bbox = compute_bbox(prev_box)
            offset = (
                center[0] - cur_center[0],
                center[1] - cur_center[1],
                prev_bbox[1][2] - cur_bbox[0][2]
            )
            translate(cur_box, offset)
        
        # add some noise
        for i in range(count):
            rotate_z(boxes[i], random.uniform(*angle_range))
            translate(boxes[i], (
                random.uniform(*jitter_range),
                random.uniform(*jitter_range),
                0
            ))
    return container, boxes


def add_random_box_stacks(
        stage,
        path: str,
        count_range=(0, 3),
    ):
    container = add_xform(stage, path)
    stacks = []
    count = random.randint(*count_range)
    for i in range(count):
        stack, items = add_random_box_stack(stage, os.path.join(path, f"stack_{i}"))
        stacks.append(stack)

    for i in range(count):
        cur_stack = stacks[i]
        cur_bbox = compute_bbox(cur_stack)
        cur_center = compute_bbox_center(cur_stack)
        translate(cur_stack, (0, -cur_center[1], -cur_bbox[0][2]))
        if i > 0:
            prev_bbox = compute_bbox(stacks[i - 1])
            translate(cur_stack, (prev_bbox[1][0] - cur_bbox[0][0], 0, 0))    
    return container, stacks
    
def add_hand_truck_with_boxes(stage, path: str):

    container = add_xform(stage, path)

    hand_truck_path = f"{path}/truck"
    box_stacks_path = f"{path}/box_stacks"

    add_usd_ref(
        stage,
        hand_truck_path,
        hand_truck_asset_url
    )

    box_stacks_container, box_stacks = add_random_box_stacks(stage, box_stacks_path, count_range=(1,4))
    rotate_z(box_stacks_container, 90)


    translate(
        box_stacks_container,
        offset=(0, random.uniform(8, 12), 28)
    )

    # remove out of bounds stacks
    last_visible = box_stacks[0]
    for i in range(len(box_stacks)):
        _, stack_bbox_max = compute_bbox(box_stacks[i])
        print(stack_bbox_max)
        if stack_bbox_max[1] > 74:
            set_visibility(box_stacks[i], "invisible")
        else:
            last_visible = box_stacks[i]
    
    # wiggle inide bounds
    boxes_bbox = compute_bbox(last_visible)
    wiggle = (82 - boxes_bbox[1][1])
    translate(box_stacks_container, (0, random.uniform(0, wiggle), 1))
    return container

stage = new_omniverse_stage()

light = add_dome_light(stage, "/scene/dome_light")
floor = add_plane(stage, "/scene/floor", size=(1000, 1000))
concrete = add_mdl_material(
    stage,
    "/scene/materials/concrete", 
    "omniverse://ov-content/Library/Materials/Base/Masonry/Concrete_Polished.mdl"
)
bind_material(floor, concrete)

all_objects_container = add_xform(stage, "/scene/objects")
for i in range(5):
    for j in range(5):
        path = f"/scene/objects/hand_truck_{i}_{j}"
        current_object = add_hand_truck_with_boxes(stage, path)
        rotate_z(current_object, random.uniform(-15, 15))
        translate(current_object, (100*i, 150*j, 0))

objects_center = compute_bbox_center(all_objects_container)
translate(all_objects_container, (-objects_center[0], -objects_center[1], 0))