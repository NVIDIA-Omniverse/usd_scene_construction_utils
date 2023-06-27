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
from pathlib import Path
sys.path.append(f"{Path.home()}/usd_scene_construction_utils") # use your install path
sys.path.append(f"{Path.home()}/usd_scene_construction_utils/examples/pallet_with_boxes") # use your install path

from usd_scene_construction_utils import *
from assets import ALL_PALLETS, SHIPPING



def add_pallet(stage, path: str):
    prim = add_usd_ref(stage, path, random.choice(ALL_PALLETS))
    add_semantics(prim, "class", "pallet")
    return prim

def add_cardboard_box(stage, path: str):
    prim = add_usd_ref(stage, path, random.choice(SHIPPING))
    add_semantics(prim, "class", "distractor")
    return prim


def add_pallet_with_box(stage, path: str):
    container = add_xform(stage, path)
    pallet = add_pallet(stage, os.path.join(path, "pallet"))
    box = add_cardboard_box(stage, os.path.join(path, "box"))
    pallet_bbox = compute_bbox(pallet)
    box_bbox = compute_bbox(box)
    translate(box,(0, 0, pallet_bbox[1][2] - box_bbox[0][2]))
    rotate_z(pallet, random.uniform(-25, 25))
    return container


def add_bush(stage, path: str):
    url = "omniverse://ov-content/Library/Assets/Vegetation/Shrub/Grass_Short_A.usd"
    return add_usd_ref(stage, path, url)


def add_tree(stage, path: str):
    url = "omniverse://ov-content/Library/Assets/Vegetation/Trees/American_Beech.usd"
    return add_usd_ref(stage, path, url)


stage = new_omniverse_stage()

brick = add_mdl_material(stage, "/scene/brick", "omniverse://ov-content/Library/Materials/Base/Masonry/Brick_Pavers.mdl")
pallet_box = add_pallet_with_box(stage, "/scene/pallet")
floor = add_plane(stage, "/scene/floor", size=(1000, 1000), uv=(20., 20.))
bush = add_bush(stage, "/scene/bush")
tree = add_tree(stage, "/scene/tree")
translate(bush, (120, 0, 0))
translate(tree, (100, -150, 0))

bind_material(floor, brick)
light = add_dome_light(stage, "/scene/dome_light")