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
from pathlib import Path
sys.path.append(f"{Path.home()}/usd_scene_construction_utils") # use your install path

from usd_scene_construction_utils import (
    new_in_memory_stage,
    add_box,
    add_camera,
    compute_look_at_matrix,
    apply_xform_matrix,
    export_stage
)


stage = new_in_memory_stage()

box = add_box(stage, "/scene/box", size=(100, 100, 100))
camera = add_camera(stage, "/scene/camera")

matrix = compute_look_at_matrix(
    at=(0, 0, 0),
    up=(0, 0, 1),
    eye=(500, 500, 500)
)

apply_xform_matrix(camera, matrix)

export_stage(stage, "add_camera.usda", default_prim="/scene")

