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
from pathlib import Path
sys.path.append(f"{Path.home()}/usd_scene_construction_utils") # use your install path

from usd_scene_construction_utils import (
    add_mdl_material,
    new_omniverse_stage,
    add_plane,
    add_box,
    stack_prims,
    bind_material,
    add_dome_light
)

stage = new_omniverse_stage()

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

# Add box
box = add_box(stage, "/scene/box", size=(100, 100, 100))

# Stack box on floor
stack_prims([floor, box], axis=2)

# Bind materials to objects
bind_material(floor, concrete)
bind_material(box, cardboard)

# Add dome light
light = add_dome_light(stage, "/scene/dome_light")