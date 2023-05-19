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
sys.path.append("/home/john/Projects/usd_scene_construction_utils") # use your install path

import random
from usd_scene_construction_utils import *

stage = new_omniverse_stage()

# Create floor
floor = add_plane(stage, "/scene/floor", (1000, 1000))

# Add a dome light
light = add_dome_light(stage, "/scene/dome_light")

# Create a grid of boxes
all_boxes = add_xform(stage, "/scene/boxes")
for i in range(5):
    for j in range(5):
        path = f"/scene/boxes/box_{i}_{j}"

        # Add box of random size
        size = (
            random.uniform(20, 50),
            random.uniform(20, 50),
            random.uniform(20, 50),
        )
        box = add_box(stage, path, size=size)

        # Set position in xy grid
        translate(box, (100*i, 100*j, 0))

        # Align z with floor
        box_min, _ = compute_bbox(box) 
        translate(box, (0, 0, -box_min[2]))

# Translate all boxes to have xy center at (0, 0)
boxes_center = compute_bbox_center(all_boxes)
translate("/scene/boxes", (-boxes_center[0], -boxes_center[1], 0))
