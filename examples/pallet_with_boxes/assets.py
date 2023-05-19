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


ALL_PALLETS = []

METAL_PALLETS = [
    "omniverse://content.ov.nvidia.com/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Shipping/Pallets/Metal/Aluminum_A/AluminumPallet_A02_PR_NVD_01.usd",
    "omniverse://content.ov.nvidia.com/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Shipping/Pallets/Metal/GalvanizedSteel_A/GalvanizedSteelPallet_A01_PR_NVD_01.usd",

]
ALL_PALLETS += METAL_PALLETS

PLASTIC_PALLETS = [
    "omniverse://content.ov.nvidia.com/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Shipping/Pallets/Plastic/ClosedDeckExport_A/ClosedDeckExportPallet_A01_PR_NVD_01.usd",
    "omniverse://content.ov.nvidia.com/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Shipping/Pallets/Plastic/Drum_A/PlasticDrumPallet_A01_PR_NVD_01.usd",
    "omniverse://content.ov.nvidia.com/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Shipping/Pallets/Plastic/Economy_A/EconomyPlasticPallet_A01_PR_NVD_01.usd",
    "omniverse://content.ov.nvidia.com/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Shipping/Pallets/Plastic/Economy_A/EconomyPlasticPallet_A02_PR_NVD_01.usd",
    "omniverse://content.ov.nvidia.com/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Shipping/Pallets/Plastic/Economy_A/EconomyPlasticPallet_A03_PR_NVD_01.usd",
    "omniverse://content.ov.nvidia.com/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Shipping/Pallets/Plastic/Export_A/ExportPallet_A01_PR_NVD_01.usd",
    "omniverse://content.ov.nvidia.com/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Shipping/Pallets/Plastic/Export_A/ExportPallet_A02_PR_NVD_01.usd",
    "omniverse://content.ov.nvidia.com/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Shipping/Pallets/Plastic/Export_A/ExportPallet_A03_PR_NVD_01.usd",
    "omniverse://content.ov.nvidia.com/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Shipping/Pallets/Plastic/Export_A/ExportPallet_A04_PR_NVD_01.usd",
    "omniverse://content.ov.nvidia.com/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Shipping/Pallets/Plastic/Export_A/ExportPallet_A05_PR_NVD_01.usd",
    "omniverse://content.ov.nvidia.com/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Shipping/Pallets/Plastic/Export_A/ExportPallet_A06_PR_NVD_01.usd",
    "omniverse://content.ov.nvidia.com/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Shipping/Pallets/Plastic/Export_A/ExportPallet_A07_PR_NVD_01.usd",
    "omniverse://content.ov.nvidia.com/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Shipping/Pallets/Plastic/HeavyDutyNestable_A/HeavyDutyNestablePallet_A01_PR_NVD_01.usd",
    "omniverse://content.ov.nvidia.com/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Shipping/Pallets/Plastic/HeavyDutyNestable_A/HeavyDutyNestablePallet_A02_PR_NVD_01.usd",
    "omniverse://content.ov.nvidia.com/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Shipping/Pallets/Plastic/Industrial_A/IndustrialPlasticPallet_A01_PR_V_NVD_01.usd",
    "omniverse://content.ov.nvidia.com/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Shipping/Pallets/Plastic/Rackable_A/RackablePallet_A01_PR_V_NVD_01.usd",
    "omniverse://content.ov.nvidia.com/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Shipping/Pallets/Plastic/Rackable_A/RackablePallet_A02_PR_V_NVD_01.usd",
    "omniverse://content.ov.nvidia.com/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Shipping/Pallets/Plastic/RackableExport_A/RackableExportPallet_A01_PR_NVD_01.usd",
    "omniverse://content.ov.nvidia.com/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Shipping/Pallets/Plastic/SolidTopRackable_A/SolidTopRackablePallet_A01_PR_V_NVD_01.usd",
    "omniverse://content.ov.nvidia.com/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Shipping/Pallets/Plastic/SolidTopRackable_A/SolidTopRackablePallet_A02_PR_V_NVD_01.usd",
    "omniverse://content.ov.nvidia.com/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Shipping/Pallets/Plastic/SolidTopRackable_A/SolidTopRackablePallet_A03_PR_V_NVD_01.usd",
    "omniverse://content.ov.nvidia.com/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Shipping/Pallets/Plastic/SolidTopRackable_A/SolidTopRackablePallet_A04_PR_V_NVD_01.usd",

]
ALL_PALLETS += PLASTIC_PALLETS

WOOD_PALLETS = [
    "omniverse://content.ov.nvidia.com/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Shipping/Pallets/Wood/Block_A/BlockPallet_A01_PR_NVD_01.usd",
    "omniverse://content.ov.nvidia.com/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Shipping/Pallets/Wood/Block_A/BlockPallet_A02_PR_NVD_01.usd",
    "omniverse://content.ov.nvidia.com/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Shipping/Pallets/Wood/Block_A/BlockPallet_A03_PR_NVD_01.usd",
    "omniverse://content.ov.nvidia.com/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Shipping/Pallets/Wood/Block_A/BlockPallet_A04_PR_NVD_01.usd",
    "omniverse://content.ov.nvidia.com/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Shipping/Pallets/Wood/Block_A/BlockPallet_A05_PR_NVD_01.usd",
    "omniverse://content.ov.nvidia.com/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Shipping/Pallets/Wood/Block_A/BlockPallet_A06_PR_NVD_01.usd",
    "omniverse://content.ov.nvidia.com/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Shipping/Pallets/Wood/Block_A/BlockPallet_A07_PR_NVD_01.usd",
    "omniverse://content.ov.nvidia.com/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Shipping/Pallets/Wood/Block_A/BlockPallet_A08_PR_NVD_01.usd",
    "omniverse://content.ov.nvidia.com/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Shipping/Pallets/Wood/Block_A/BlockPallet_A09_PR_NVD_01.usd",
    "omniverse://content.ov.nvidia.com/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Shipping/Pallets/Wood/Block_B/BlockPallet_B01_PR_NVD_01.usd",
    "omniverse://content.ov.nvidia.com/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Shipping/Pallets/Wood/Block_B/BlockPallet_B02_PR_NVD_01.usd",
    "omniverse://content.ov.nvidia.com/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Shipping/Pallets/Wood/Block_B/BlockPallet_B03_PR_NVD_01.usd",
    "omniverse://content.ov.nvidia.com/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Shipping/Pallets/Wood/Block_C/BlockPallet_C01_PR_NVD_01.usd",
    "omniverse://content.ov.nvidia.com/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Shipping/Pallets/Wood/Drum_A/WoodDrumPallet_A01_PR_NVD_01.usd",
    "omniverse://content.ov.nvidia.com/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Shipping/Pallets/Wood/Drum_A/WoodDrumPallet_A02_PR_NVD_01.usd",
    "omniverse://content.ov.nvidia.com/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Shipping/Pallets/Wood/Drum_A/WoodDrumPallet_A03_PR_NVD_01.usd",
    "omniverse://content.ov.nvidia.com/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Shipping/Pallets/Wood/Drum_A/WoodDrumPallet_A04_PR_NVD_01.usd",
    "omniverse://content.ov.nvidia.com/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Shipping/Pallets/Wood/Drum_A/WoodDrumPallet_A05_PR_NVD_01.usd",
    "omniverse://content.ov.nvidia.com/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Shipping/Pallets/Wood/Drum_A/WoodDrumPallet_A06_PR_NVD_01.usd",
    "omniverse://content.ov.nvidia.com/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Shipping/Pallets/Wood/Drum_A/WoodDrumPallet_A07_PR_NVD_01.usd",
    "omniverse://content.ov.nvidia.com/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Shipping/Pallets/Wood/Drum_A/WoodDrumPallet_A08_PR_NVD_01.usd",
    "omniverse://content.ov.nvidia.com/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Shipping/Pallets/Wood/Pressed_A/PressedWoodPallet_A01_PR_NVD_01.usd",
    "omniverse://content.ov.nvidia.com/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Shipping/Pallets/Wood/Pressed_A/PressedWoodPallet_A02_PR_NVD_01.usd",
    "omniverse://content.ov.nvidia.com/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Shipping/Pallets/Wood/Pressed_A/PressedWoodPallet_A03_PR_NVD_01.usd",
    "omniverse://content.ov.nvidia.com/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Shipping/Pallets/Wood/Pressed_A/PressedWoodPallet_A04_PR_NVD_01.usd",
    "omniverse://content.ov.nvidia.com/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Shipping/Pallets/Wood/Pressed_A/PressedWoodPallet_A05_PR_NVD_01.usd",
    "omniverse://content.ov.nvidia.com/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Shipping/Pallets/Wood/Pressed_A/PressedWoodPallet_A06_PR_NVD_01.usd",
    "omniverse://content.ov.nvidia.com/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Shipping/Pallets/Wood/Pressed_A/PressedWoodPallet_A07_PR_NVD_01.usd",
    "omniverse://content.ov.nvidia.com/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Shipping/Pallets/Wood/Pressed_A/PressedWoodPallet_A08_PR_NVD_01.usd",
    "omniverse://content.ov.nvidia.com/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Shipping/Pallets/Wood/Pressed_A/PressedWoodPallet_A09_PR_NVD_01.usd",
    "omniverse://content.ov.nvidia.com/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Shipping/Pallets/Wood/Recycled_A/RecycledWoodPallet_A01_PR_NVD_01.usd",
    "omniverse://content.ov.nvidia.com/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Shipping/Pallets/Wood/Recycled_A/RecycledWoodPallet_A02_PR_NVD_01.usd",
    "omniverse://content.ov.nvidia.com/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Shipping/Pallets/Wood/Recycled_A/RecycledWoodPallet_A03_PR_NVD_01.usd",
    "omniverse://content.ov.nvidia.com/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Shipping/Pallets/Wood/Recycled_A/RecycledWoodPallet_A04_PR_NVD_01.usd",
    "omniverse://content.ov.nvidia.com/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Shipping/Pallets/Wood/Recycled_A/RecycledWoodPallet_A05_PR_NVD_01.usd",
    "omniverse://content.ov.nvidia.com/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Shipping/Pallets/Wood/Recycled_A/RecycledWoodPallet_A06_PR_NVD_01.usd",
    "omniverse://content.ov.nvidia.com/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Shipping/Pallets/Wood/Recycled_A/RecycledWoodPallet_A07_PR_NVD_01.usd",
    "omniverse://content.ov.nvidia.com/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Shipping/Pallets/Wood/Recycled_A/RecycledWoodPallet_A08_PR_NVD_01.usd",
    "omniverse://content.ov.nvidia.com/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Shipping/Pallets/Wood/Wing_A/WingPallet_A01_PR_NVD_01.usd",

]
ALL_PALLETS += WOOD_PALLETS

ALL_DISTRACTORS = []

SAFETY = [
    "omniverse://content.ov.nvidia.com/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Safety/Cones/Colored_Sport/ColoredSportTrafficCone_A01_46cm_PR_V_NVD_01.usd",
    "omniverse://content.ov.nvidia.com/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Safety/Cones/Colored_Traffic/ColoredTrafficCone_A01_71cm_PR_V_NVD_01.usd",
    "omniverse://content.ov.nvidia.com/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Safety/Cones/Heavy-Duty_Traffic/HeavyDutyTrafficCone_A_PR_V_NVD_01.usd",
    "omniverse://content.ov.nvidia.com/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Safety/Cones/Pop-Up_Traffic/PopUpCone_A01_05cm_PR_NVD_01.usd",
    "omniverse://content.ov.nvidia.com/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Safety/Cones/Traffic/TrafficCone_A_PR_V_NVD_01.usd",
    "omniverse://content.ov.nvidia.com/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Safety/Floor_Signs/FoldingWarning_A/FoldingWarningSign_A01_PR_NVD_01.usd",
    "omniverse://content.ov.nvidia.com/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Safety/Floor_Signs/MobileShutOffSystem_A/MobileShutOffSystem_A02_PR_NVD_01.usd",
    "omniverse://content.ov.nvidia.com/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Safety/Floor_Signs/Movable_A/FloorSignMovable_PR_NVD_01.usd",
    "omniverse://content.ov.nvidia.com/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Safety/Floor_Signs/Warning_A/WarningSign_A01_PR_NVD_01.usd",
    "omniverse://content.ov.nvidia.com/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Safety/Floor_Signs/WetFloor_B/WetFloorSign_B01_PR_NVD_01.usd",
 

]
ALL_DISTRACTORS += SAFETY

SHIPPING = [
    "omniverse://content.ov.nvidia.com/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Shipping/Cardboard_Boxes/Cube_A/CubeBox_A01_10cm_PR_NVD_01.usd",
    "omniverse://content.ov.nvidia.com/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Shipping/Cardboard_Boxes/Flat_A/FlatBox_A01_15x16x6cm_PR_NVD_01.usd",
    "omniverse://content.ov.nvidia.com/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Shipping/Cardboard_Boxes/Long_A/LongBox_A02_21x51x11xcm_PR_NVD_01.usd",
    "omniverse://content.ov.nvidia.com/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Shipping/Cardboard_Boxes/Multi-Depth_A/MultiDepthBox_A02_20x25x20cm_PR_NVD_01.usd",
    "omniverse://content.ov.nvidia.com/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Shipping/Cardboard_Boxes/Multi-Depth_A/MultiDepthBox_A03_25x25x31cm_PR_NVD_01.usd",
    "omniverse://content.ov.nvidia.com/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Shipping/Cardboard_Boxes/Printer_A/PrintersBox_A02_21x28x10cm_PR_NVD_01.usd",
    "omniverse://content.ov.nvidia.com/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Shipping/Cardboard_Boxes/Printer_A/PrintersBox_A01_28x44x25cm_PR_NVD_01.usd",
    "omniverse://content.ov.nvidia.com/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Shipping/Cardboard_Boxes/White_A/WhiteCorrugatedBox_A01_10x10x10cm_PR_NVD_01.usd",
]
ALL_DISTRACTORS += SHIPPING

WOOD_CRATES = [
    "omniverse://content.ov.nvidia.com/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Shipping/Wood_Crates/HeavyDuty_A/HeavyDutyWoodCrate_A01_90x90x80cm_PR_NV_01.usd",
    "omniverse://content.ov.nvidia.com/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Shipping/Wood_Crates/HeavyDuty_A/HeavyDutyWoodCrate_A03_120x120x110cm_PR_NV_01.usd",

]
ALL_DISTRACTORS += WOOD_CRATES

BINS = [
    "omniverse://content.ov.nvidia.com/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Storage/Bins/Bin_A/Bin_A01_10x08x08cm_PR_V_NVD_01.usd",
    "omniverse://content.ov.nvidia.com/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Storage/Bins/Bin_A/Bin_A04_14x30x13cm_PR_V_NVD_01.usd",
    "omniverse://content.ov.nvidia.com/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Storage/Bins/Bin_B/Bin_B01_10x10x10cm_PR_V_NVD_01.usd",
    "omniverse://content.ov.nvidia.com/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Storage/Bins/Bin_B/Bin_B06_45x71x32cm_PR_V_NVD_01.usd",

]
ALL_DISTRACTORS += BINS

BOTTLES = [
    # "omniverse://content.ov.nvidia.com/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Storage/Bottles/Plastic/NaturalBostonRound_A/NaturalBostonRoundBottle_A01_PR_NVD_01.usd",
    # "omniverse://content.ov.nvidia.com/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Storage/Bottles/Plastic/NaturalBostonRound_A/NaturalBostonRoundBottle_A02_PR_NVD_01.usd",
]
ALL_DISTRACTORS += BOTTLES

BOXES = [
    "omniverse://content.ov.nvidia.com/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Storage/Boxes/Box_A/Box_A01_60x40x32cm_PR_V_NVD_01.usd",
    "omniverse://content.ov.nvidia.com/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Storage/Boxes/Box_A/Box_A08_60x41x07cm_PR_V_NVD_01.usd",
    "omniverse://content.ov.nvidia.com/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Storage/Boxes/Box_A/Box_A11_40x30x23cm_PR_V_NVD_01.usd",


]
ALL_DISTRACTORS += BOXES

CASES = [
    "omniverse://content.ov.nvidia.com/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Storage/Cases/Case_A/Case_A02_60x42x26cm_PR_V_NVD_01.usd",
    "omniverse://content.ov.nvidia.com/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Storage/Cases/Case_C/Case_C02_82x43x36cm_PR_V_NVD_01.usd",
    "omniverse://content.ov.nvidia.com/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Storage/Cases/Case_D/Case_D01_42x31x35cm_PR_V_NVD_01.usd",
    "omniverse://content.ov.nvidia.com/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Storage/Cases/Case_E/Case_E01_46x28x21cm_PR_V_NVD_01.usd",

]
ALL_DISTRACTORS += CASES

CONTAINERS = [
    "omniverse://content.ov.nvidia.com/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Storage/Containers/Container_A/Container_A01_46x33x24cm_PR_V_NVD_01.usd",
    "omniverse://content.ov.nvidia.com/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Storage/Containers/Container_B/Container_B02_40x30x06cm_PR_V_NVD_01.usd",
    "omniverse://content.ov.nvidia.com/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Storage/Containers/Container_B/Container_B01_41x30x08cm_PR_V_NVD_01.usd",
    "omniverse://content.ov.nvidia.com/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Storage/Containers/Container_D/Container_D07_118x70x56cm_PR_V_NVD_01.usd",
    "omniverse://content.ov.nvidia.com/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Storage/Containers/Container_E/Container_E03_120x82x55cm_PR_V_NVD_01.usd",
    "omniverse://content.ov.nvidia.com/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Storage/Containers/Container_E/Container_E06_120x82x45cm_PR_V_NVD_01.usd",
    "omniverse://content.ov.nvidia.com/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Storage/Containers/Container_H/Container_H01_60x40x25cm_PR_V_NVD_01.usd",
    "omniverse://content.ov.nvidia.com/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Storage/Containers/Container_I/Container_I04_160x120x64cm_PR_V_NVD_01.usd",
]
ALL_DISTRACTORS += CONTAINERS

DRUMS = [
    "omniverse://content.ov.nvidia.com/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Storage/Drums/Fiber_A/FiberDrum_A01_PR_NVD_01.usd",
    # "omniverse://content.ov.nvidia.com/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Storage/Drums/Plastic_B/PlasticDrum_B03_PR_NVD_01.usd",

]
ALL_DISTRACTORS += DRUMS


PAILS = [
    # "omniverse://content.ov.nvidia.com/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Storage/Pails/Plastic_A/PlasticPail_A01_PR_V_NVD_01.usd"
]
ALL_DISTRACTORS += PAILS

TOTES = [
    "omniverse://content.ov.nvidia.com/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Storage/Totes/Tote_A/Tote_A02_82x60x51cm_PR_V_NVD_01.usd",
    "omniverse://content.ov.nvidia.com/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Storage/Totes/Tote_A/Tote_A03_82x60x33cm_PR_V_NVD_01.usd",
    "omniverse://content.ov.nvidia.com/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Storage/Totes/Tote_E/Tote_E04_76x54x37cm_PR_V_NVD_01.usd",

]
ALL_DISTRACTORS += TOTES

YCB = [
    "omniverse://content.ov.nvidia.com/NVIDIA/Assets/Isaac/2022.2.1/Isaac/Props/YCB/Axis_Aligned/002_master_chef_can.usd",
    "omniverse://content.ov.nvidia.com/NVIDIA/Assets/Isaac/2022.2.1/Isaac/Props/YCB/Axis_Aligned/003_cracker_box.usd",
    "omniverse://content.ov.nvidia.com/NVIDIA/Assets/Isaac/2022.2.1/Isaac/Props/YCB/Axis_Aligned/004_sugar_box.usd",
    "omniverse://content.ov.nvidia.com/NVIDIA/Assets/Isaac/2022.2.1/Isaac/Props/YCB/Axis_Aligned/005_tomato_soup_can.usd",
    "omniverse://content.ov.nvidia.com/NVIDIA/Assets/Isaac/2022.2.1/Isaac/Props/YCB/Axis_Aligned/006_mustard_bottle.usd",
    "omniverse://content.ov.nvidia.com/NVIDIA/Assets/Isaac/2022.2.1/Isaac/Props/YCB/Axis_Aligned/007_tuna_fish_can.usd",
    "omniverse://content.ov.nvidia.com/NVIDIA/Assets/Isaac/2022.2.1/Isaac/Props/YCB/Axis_Aligned/009_gelatin_box.usd",
    "omniverse://content.ov.nvidia.com/NVIDIA/Assets/Isaac/2022.2.1/Isaac/Props/Dolly/dolly_physics.usd",

]
ALL_DISTRACTORS += YCB