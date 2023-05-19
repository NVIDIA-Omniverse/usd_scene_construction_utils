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


import os
import numpy as np
import math
from typing import Optional, Sequence, Tuple 
from typing_extensions import Literal

from pxr import Gf, Sdf, Usd, UsdGeom, UsdLux, UsdShade


def new_in_memory_stage() -> Usd.Stage:
    """Creates a new in memory USD stage.
    
    Returns:
        Usd.Stage:  The USD stage.
    """

    stage = Usd.Stage.CreateInMemory()
    UsdGeom.SetStageUpAxis(stage, UsdGeom.Tokens.z)

    return stage


def new_omniverse_stage() -> Usd.Stage:
    """Creates a new Omniverse USD stage.
    
    This method creates a new Omniverse USD stage.  This will clear the active
    omniverse stage, replacing it with a new one.

    Returns:
        Usd.Stage:  The Omniverse USD stage.
    """

    try:
        import omni.usd
    except ImportError:
        raise ImportError("Omniverse not found.  This method is unavailable.")

    omni.usd.get_context().new_stage()
    stage = omni.usd.get_context().get_stage()

    UsdGeom.SetStageUpAxis(stage, UsdGeom.Tokens.z)

    return stage


def get_omniverse_stage() -> Usd.Stage:
    """Returns the current Omniverse USD stage.
    
    Returns:
        Usd.Stage:  The currently active Omniverse USD stage.
    """

    try:
        import omni.usd
    except ImportError:
        raise ImportError("Omniverse not found.  This method is unavailable.")

    stage = omni.usd.get_context().get_stage()

    return stage


def add_usd_ref(stage: Usd.Stage, path: str, usd_path: str) -> Usd.Prim:
    """Adds an external USD reference to a USD stage.
    
    Args:
        stage (:class:`Usd.Stage`): The USD stage to modify.
        path (str): The path to add the USD reference.
        usd_path (str): The filepath or URL of the USD reference (ie: a Nucleus
            server URL).

    Returns:
        Usd.Prim: The created USD prim.
    """

    stage.DefinePrim(path, "Xform")
    prim_ref = stage.DefinePrim(os.path.join(path, "ref"))
    prim_ref.GetReferences().AddReference(usd_path)

    return get_prim(stage, path)

def _make_box_mesh(size: Tuple[float, float, float]):

    # private utility function used by make_box

    numFaces = 6
    numVertexPerFace = 4

    # Generate vertices on box
    vertices = []
    for i in [-1, 1]:
        for j in [-1, 1]:
            for k in [-1, 1]:
                vertices.append((i * size[0], j * size[1], k * size[2]))
    
    # Make faces for box (ccw convention)
    faceVertexCounts = [numVertexPerFace] * numFaces
    faceVertexIndices = [
        2, 0, 1, 3,
        4, 6, 7, 5,
        0, 4, 5, 1,
        6, 2, 3, 7,
        0, 2, 6, 4,
        5, 7, 3, 1,
    ]

    # Make normals for face vertices
    _faceVertexNormals = [
        (-1, 0, 0),
        (1, 0, 0),
        (0, -1, 0),
        (0, 1, 0),
        (0, 0, -1),
        (0, 0, 1),
    ]
    faceVertexNormals = []
    for n in _faceVertexNormals:
        for i in range(numVertexPerFace):
            faceVertexNormals.append(n)


    # Assign uv-mapping for face vertices
    _faceUvMaps = [
        (0, 0), (1, 0), (1, 1), (0, 1)
    ]
    faceUvMaps = []
    for i in range(numFaces):
        for uvm in _faceUvMaps:
            faceUvMaps.append(uvm)

    return (vertices, faceVertexCounts, faceVertexIndices, faceVertexNormals, 
        faceUvMaps)


def add_box(stage: Usd.Stage, path: str, size: Tuple[float, float, float]) -> Usd.Prim:
    """Adds a 3D box to a USD stage.
    
    This adds a 3D box to the USD stage.  The box is created with it's center
    at (x, y, z) = (0, 0, 0).

    Args:
        stage (:class:`Usd.Stage`): The USD stage to modify.
        path (str): The path to add the USD prim.
        size (Tuple[float, float, float]): The size of the box (x, y, z sizes).

    Returns:
        Usd.Prim: The created USD prim.
    """

    half_size = (size[0] / 2, size[1] / 2, size[2] / 2)

    stage.DefinePrim(path, "Xform")

    (vertices, faceVertexCounts, faceVertexIndices, faceVertexNormals, 
        faceUvMaps) = _make_box_mesh(half_size)

    # create mesh at {path}/mesh, but return prim at {path}
    prim: UsdGeom.Mesh = UsdGeom.Mesh.Define(stage, os.path.join(path, "mesh"))
    prim.CreateExtentAttr().Set([
        (-half_size[0], -half_size[1], -half_size[2]),
        (half_size[0], half_size[1], half_size[2])
    ])
    prim.CreateFaceVertexCountsAttr().Set(faceVertexCounts)
    prim.CreateFaceVertexIndicesAttr().Set(faceVertexIndices)

    var = UsdGeom.Primvar(prim.CreateNormalsAttr())
    var.Set(faceVertexNormals)
    var.SetInterpolation(UsdGeom.Tokens.faceVarying)

    var = UsdGeom.PrimvarsAPI(prim).CreatePrimvar("primvars:st", Sdf.ValueTypeNames.Float2Array)
    var.Set(faceUvMaps)
    var.SetInterpolation(UsdGeom.Tokens.faceVarying)

    prim.CreatePointsAttr().Set(vertices)
    prim.CreateSubdivisionSchemeAttr().Set(UsdGeom.Tokens.none)

    return get_prim(stage, path)


def add_xform(stage: Usd.Stage, path: str):
    """Adds a USD transform (Xform) to a USD stage.
    
    This method adds a USD Xform to the USD stage at a given path.  This is
    helpful when you want to add hierarchy to a scene.  After you create a 
    transform, any USD prims located under the transform path will be children
    of the transform and can be moved as a group.

    Args:
        stage (:class:`Usd.Stage`): The USD stage to modify.
        path (str): The path to add the USD prim.   

    Returns:
        Usd.Prim: The created USD prim.
    """

    stage.DefinePrim(path, "Xform")
    return get_prim(stage, path)


def add_plane(
        stage: Usd.Stage, 
        path: str, 
        size: Tuple[float, float],
        uv: Tuple[float, float]=(1, 1)):
    """Adds a 2D plane to a USD stage.
    
    Args:
        stage (Usd.Stage): The USD stage to modify.
        path (str): The path to add the USD prim.
        size (Tuple[float, float]): The size of the 2D plane (x, y).
        uv (Tuple[float, float]): The UV mapping for textures applied to the 
            plane.  For example, uv=(1, 1), means the texture will be spread
            to fit the full size of the plane.  uv=(10, 10) means the texture
            will repeat 10 times along each dimension. uv=(5, 10) means the
            texture will be scaled to repeat 5 times along the x dimension and
            10 times along the y direction.
    
    Returns:
        Usd.Prim: The created USD prim.
    """

    stage.DefinePrim(path, "Xform")
    
    # create mesh at {path}/mesh, but return prim at {path}
    prim: UsdGeom.Mesh = UsdGeom.Mesh.Define(stage, os.path.join(path, "mesh"))
    prim.CreateExtentAttr().Set([
        (-size[0], -size[1], 0),
        (size[0], size[1], 0)
    ])
    prim.CreateFaceVertexCountsAttr().Set([4])
    prim.CreateFaceVertexIndicesAttr().Set([0, 1, 3, 2])

    var = UsdGeom.Primvar(prim.CreateNormalsAttr())
    var.Set([(0, 0, 1)] * 4)
    var.SetInterpolation(UsdGeom.Tokens.faceVarying)

    var = UsdGeom.PrimvarsAPI(prim).CreatePrimvar("primvars:st", 
        Sdf.ValueTypeNames.Float2Array)

    var.Set(
        [(0, 0), (uv[0], 0), (uv[0], uv[1]), (0, uv[1])]
    )
    var.SetInterpolation(UsdGeom.Tokens.faceVarying)

    prim.CreatePointsAttr().Set([
        (-size[0], -size[1], 0),
        (size[0], -size[1], 0),
        (-size[0], size[1], 0),
        (size[0], size[1], 0),
    ])
    prim.CreateSubdivisionSchemeAttr().Set(UsdGeom.Tokens.none)

    return get_prim(stage, path)

def add_dome_light(stage: Usd.Stage, path: str, intensity: float = 1000, 
        angle: float = 180, exposure: float=0.) -> UsdLux.DomeLight:
    """Adds a dome light to a USD stage.
    
    Args:
        stage (Usd.Stage): The USD stage to modify.
        path (str): The path to add the USD prim.
        intensity (float): The intensity of the dome light (default 1000).
        angle (float): The angle of the dome light (default 180)
        exposure (float): THe exposure of the dome light (default 0)

    Returns:
        UsdLux.DomeLight:  The created Dome light.
    """

    light = UsdLux.DomeLight.Define(stage, path)

    # intensity
    light.CreateIntensityAttr().Set(intensity)
    light.CreateTextureFormatAttr().Set(UsdLux.Tokens.latlong)
    light.CreateExposureAttr().Set(exposure)

    # cone angle
    shaping = UsdLux.ShapingAPI(light)
    shaping.Apply(light.GetPrim())
    shaping.CreateShapingConeAngleAttr().Set(angle)
    shaping.CreateShapingConeSoftnessAttr()
    shaping.CreateShapingFocusAttr()
    shaping.CreateShapingFocusTintAttr()
    shaping.CreateShapingIesFileAttr()

    return light

def add_sphere_light(stage: Usd.Stage, path: str, intensity=30000, 
        radius=50, angle=180, exposure=0.):
    """Adds a sphere light to a USD stage.
    
    Args:
        stage (Usd.Stage): The USD stage to modify.
        path (str): The path to add the USD prim.
        radius (float): The radius of the sphere light
        intensity (float): The intensity of the sphere light (default 1000).
        angle (float): The angle of the sphere light (default 180)
        exposure (float): THe exposure of the sphere light (default 0)

    Returns:
        UsdLux.SphereLight:  The created sphere light.
    """

    light = UsdLux.SphereLight.Define(stage, path)

    # intensity
    light.CreateIntensityAttr().Set(intensity)
    light.CreateRadiusAttr().Set(radius)
    light.CreateExposureAttr().Set(exposure)

    # cone angle
    shaping = UsdLux.ShapingAPI(light)
    shaping.Apply(light.GetPrim())
    shaping.CreateShapingConeAngleAttr().Set(angle)
    shaping.CreateShapingConeSoftnessAttr()
    shaping.CreateShapingFocusAttr()
    shaping.CreateShapingFocusTintAttr()
    shaping.CreateShapingIesFileAttr()

    return light

def add_mdl_material(stage: Usd.Stage, path: str, material_url: str, 
        material_name: Optional[str] = None) -> UsdShade.Material:
    """Adds an Omniverse MDL material to a USD stage.
    
    *Omniverse only*

    Args:
        stage (Usd.Stage): The USD stage to modify.
        path (str): The path to add the USD prim.
        material_url (str): The URL of the material, such as on a Nucelus server.
        material_name (Optional[str]): An optional name to give the material.  If 
            one is not provided, it will default to the filename of the material
            URL (excluding the extension).

    returns:
        UsdShade.Material:  The created USD material.
    """

    try:
        import omni.usd
    except ImportError:
        raise ImportError("Omniverse not found.  This method is unavailable.")

    # Set default mtl_name
    if material_name is None:
        material_name = os.path.basename(material_url).split('.')[0]

    # Create material using omniverse kit
    if not stage.GetPrimAtPath(path):
        success, result = omni.kit.commands.execute(
            "CreateMdlMaterialPrimCommand",
            mtl_url=material_url,
            mtl_name=material_name,
            mtl_path=path
        )

    # Get material from stage
    material = UsdShade.Material(stage.GetPrimAtPath(path))

    return material

def add_camera(
        stage: Usd.Stage, 
        path: str,
        focal_length: float = 35,
        horizontal_aperature: float = 20.955,
        vertical_aperature: float = 20.955,
        clipping_range: Tuple[float, float] = (0.1, 100000)
    ) -> UsdGeom.Camera:
    """Adds a camera to a USD stage.
    

    Args:
        stage (Usd.Stage): The USD stage to modify.
        path (str): The path to add the USD prim.
        focal_length (float): The focal length of the camera (default 35).
        horizontal_aperature (float): The horizontal aperature of the camera
            (default 20.955).
        vertical_aperature (float): The vertical aperature of the camera
            (default 20.955).
        clipping_range (Tuple[float, float]): The clipping range of the camera.

    returns:
        UsdGeom.Camera:  The created USD camera.
    """

    camera = UsdGeom.Camera.Define(stage, path)
    camera.CreateFocalLengthAttr().Set(focal_length)
    camera.CreateHorizontalApertureAttr().Set(horizontal_aperature)
    camera.CreateVerticalApertureAttr().Set(vertical_aperature)
    camera.CreateClippingRangeAttr().Set(clipping_range)

    return camera

def get_prim(stage: Usd.Stage, path: str) -> Usd.Prim:
    """Returns a prim at the specified path in a USD stage.
    
    Args:
        stage (Usd.Stage): The USD stage to query.
        path (str): The path of the prim.

    Returns:
        Usd.Prim:  The USD prim at the specified path.
    """
    return stage.GetPrimAtPath(path)


def get_material(stage: Usd.Stage, path: str) -> UsdShade.Material:
    """Returns a material at the specified path in a USD stage.
    
    Args:
        stage (Usd.Stage): The USD stage to query.
        path (str): The path of the material.

    Returns:
        UsdShade.Material:  The USD material at the specified path.
    """
    prim = get_prim(stage, path)
    return UsdShade.Material(prim)


def export_stage(stage: Usd.Stage, filepath: str, default_prim=None):
    """Exports a USD stage to a given filepath.
    
    Args:
        stage (Usd.Stage): The USD stage to export.
        path (str):  The filepath to export the USD stage to.
        default_prim (Optional[str]):  The path of the USD prim in the
            stage to set as the default prim.  This is useful when you
            want to use the exported USD as a reference, or when you want
            to place the USD in Omniverse.
    """
    if default_prim is not None:
        stage.SetDefaultPrim(get_prim(stage, default_prim))
    stage.Export(filepath)


def add_semantics(prim: Usd.Prim, type: str, name: str):
    """Adds semantics to a USD prim.
    
    This function adds semantics to a USD prim.  This is useful for assigning
    classes to objects when generating synthetic data with Omniverse Replicator.

    For example:

    add_semantics(dog_prim, "class", "dog")
    add_semantics(cat_prim, "class", "cat")

    Args:
        prim (Usd.Prim):  The USD prim to modify.
        type (str):  The semantics type.  This depends on how the data is ingested.
            Typically, when using Omniverse replicator you will set this to "class".
        name (str):  The value of the semantic type.  Typically, this would 
            correspond to the class label.

    Returns:
        Usd.Prim:  The USD prim with added semantics.
    """

    prim.AddAppliedSchema(f"SemanticsAPI:{type}_{name}")

    prim.CreateAttribute(f"semantic:{type}_{name}:params:semanticType", 
        Sdf.ValueTypeNames.String).Set(type)

    prim.CreateAttribute(f"semantic:{type}_{name}:params:semanticData", 
        Sdf.ValueTypeNames.String).Set(name)

    return prim


def bind_material(prim: Usd.Prim, material: UsdShade.Material):
    """Binds a USD material to a USD prim.
    
    Args:
        prim (Usd.Prim):  The USD prim to modify.
        material (UsdShade.Material):  The USD material to bind to the USD prim.

    Returns:
        Usd.Prim:  The modified USD prim with the specified material bound to it.
    """

    prim.ApplyAPI(UsdShade.MaterialBindingAPI)
    UsdShade.MaterialBindingAPI(prim).Bind(material, 
        UsdShade.Tokens.strongerThanDescendants)

    return prim


def collapse_xform(prim: Usd.Prim):
    """Collapses all xforms on a given USD prim.
    
    This method collapses all Xforms on a given prim.  For example,
    a series of rotations, translations would be combined into a single matrix
    operation.

    Args:
        prim (Usd.Prim):  The Usd.Prim to collapse the transforms of.
    
    Returns:
        Usd.Prim:  The Usd.Prim.
    """

    x = UsdGeom.Xformable(prim)
    local = x.GetLocalTransformation()
    prim.RemoveProperty("xformOp:translate")
    prim.RemoveProperty("xformOp:transform")
    prim.RemoveProperty("xformOp:rotateX")
    prim.RemoveProperty("xformOp:rotateY")
    prim.RemoveProperty("xformOp:rotateZ")
    var = x.MakeMatrixXform()
    var.Set(local)

    return prim


def get_xform_op_order(prim: Usd.Prim):
    """Returns the order of Xform ops on a given prim."""
    x = UsdGeom.Xformable(prim)
    op_order = x.GetXformOpOrderAttr().Get()
    if op_order is not None:
        op_order = list(op_order)
        return op_order
    else:
        return []


def set_xform_op_order(prim: Usd.Prim, op_order: Sequence[str]):
    """Sets the order of Xform ops on a given prim"""
    x = UsdGeom.Xformable(prim)
    x.GetXformOpOrderAttr().Set(op_order)
    return prim


def xform_op_move_end_to_front(prim: Usd.Prim):
    """Pops the last xform op on a given prim and adds it to the front."""
    order = get_xform_op_order(prim)
    end = order.pop(-1)
    order.insert(0, end)
    set_xform_op_order(prim, order)
    return prim


def get_num_xform_ops(prim: Usd.Prim) -> int:
    """Returns the number of xform ops on a given prim."""
    return len(get_xform_op_order(prim))


def apply_xform_matrix(prim: Usd.Prim, transform: np.ndarray):
    """Applies a homogeneous transformation matrix to the current prim's xform list.

    Args:
        prim (Usd.Prim):  The USD prim to transform.
        transform (np.ndarray):  The 4x4 homogeneous transform matrix to apply.

    Returns:
        Usd.Prim:  The modified USD prim with the provided transform applied after current transforms.
    """
    x = UsdGeom.Xformable(prim)
    x.AddTransformOp(opSuffix=f"num_{get_num_xform_ops(prim)}").Set(
        Gf.Matrix4d(transform)
    )
    xform_op_move_end_to_front(prim)
    return prim


def scale(prim: Usd.Prim, scale: Tuple[float, float, float]):
    """Scales a prim along the (x, y, z) dimensions.
    
    Args:
        prim (Usd.Prim):  The USD prim to scale.
        scale (Tuple[float, float, float]):  The scaling factors for the (x, y, z) dimensions.

    Returns:
        Usd.Prim:  The scaled prim.
    """
    x = UsdGeom.Xformable(prim)
    x.AddScaleOp(opSuffix=f"num_{get_num_xform_ops(prim)}").Set(scale)
    xform_op_move_end_to_front(prim)
    return prim


def translate(prim: Usd.Prim, offset: Tuple[float, float, float]):
    """Translates a prim along the (x, y, z) dimensions.
    
    Args:
        prim (Usd.Prim):  The USD prim to translate.
        offset (Tuple[float, float, float]):  The offsets for the (x, y, z) dimensions.

    Returns:
        Usd.Prim:  The translated prim.
    """
    x = UsdGeom.Xformable(prim)
    x.AddTranslateOp(opSuffix=f"num_{get_num_xform_ops(prim)}").Set(offset)
    xform_op_move_end_to_front(prim)
    return prim


def rotate_x(prim: Usd.Prim, angle: float):
    """Rotates a prim around the X axis.
    
    Args:
        prim (Usd.Prim):  The USD prim to rotate.
        angle (float):  The rotation angle in degrees.

    Returns:
        Usd.Prim:  The rotated prim.
    """
    x = UsdGeom.Xformable(prim)
    x.AddRotateXOp(opSuffix=f"num_{get_num_xform_ops(prim)}").Set(angle)
    xform_op_move_end_to_front(prim)
    return prim

    
def rotate_y(prim: Usd.Prim, angle: float):
    """Rotates a prim around the Y axis.
    
    Args:
        prim (Usd.Prim):  The USD prim to rotate.
        angle (float):  The rotation angle in degrees.

    Returns:
        Usd.Prim:  The rotated prim.
    """
    x = UsdGeom.Xformable(prim)
    x.AddRotateYOp(opSuffix=f"num_{get_num_xform_ops(prim)}").Set(angle)
    xform_op_move_end_to_front(prim)
    return prim


def rotate_z(prim: Usd.Prim, angle: float):
    """Rotates a prim around the Z axis.
    
    Args:
        prim (Usd.Prim):  The USD prim to rotate.
        angle (float):  The rotation angle in degrees.

    Returns:
        Usd.Prim:  The rotated prim.
    """
    x = UsdGeom.Xformable(prim)
    x.AddRotateZOp(opSuffix=f"num_{get_num_xform_ops(prim)}").Set(angle)
    xform_op_move_end_to_front(prim)
    return prim


def stack_prims(prims: Sequence[Usd.Prim], axis: int = 2, gap: float = 0, align_center=False):
    """Stacks prims on top of each other (or side-by-side).

    This function stacks prims by placing them so their bounding boxes 
    are adjacent along a given axis.

    Args:
        prim (Usd.Prim):  The USD prims to stack.
        axis (int): The axis along which to stack the prims. x=0, y=1, z=2. Default 2.
        gap (float):  The spacing to add between stacked elements.

    Returns:
        Sequence[Usd.Prim]: The stacked prims.
    """

    for i in range(1, len(prims)):
        prev = prims[i - 1]
        cur = prims[i]
        bb_cur_min, bb_cur_max = compute_bbox(cur)
        bb_prev_min, bb_prev_max = compute_bbox(prev)
        
        if align_center:
            offset  = [
                (bb_cur_max[0] + bb_cur_min[0]) / 2. - (bb_prev_max[0] + bb_prev_min[0]) / 2.,
                (bb_cur_max[1] + bb_cur_min[1]) / 2. - (bb_prev_max[1] + bb_prev_min[1]) / 2.,
                (bb_cur_max[2] + bb_cur_min[2]) / 2. - (bb_prev_max[2] + bb_prev_min[2]) / 2.
            ]
        else:
            offset = [0, 0, 0]
        offset[axis] = bb_prev_max[axis] - bb_cur_min[axis]

        if isinstance(gap, list):
            offset[axis] = offset[axis] + gap[i]
        else:
            offset[axis] = offset[axis] + gap

        translate(cur, tuple(offset))

    return prims


def compute_bbox(prim: Usd.Prim) -> \
        Tuple[Tuple[float, float, float], Tuple[float, float, float]]:
    """Computes the axis-aligned bounding box for a USD prim.
    
    Args:
        prim (Usd.Prim):  The USD prim to compute the bounding box of.

    Returns:
        Tuple[Tuple[float, float, float], Tuple[float, float, float]] The ((min_x, min_y, min_z), (max_x, max_y, max_z)) values of the bounding box.
    """
    
    bbox_cache: UsdGeom.BBoxCache = UsdGeom.BBoxCache(
        time=Usd.TimeCode.Default(),
        includedPurposes=[UsdGeom.Tokens.default_],
        useExtentsHint=True
    )

    total_bounds = Gf.BBox3d()

    for p in Usd.PrimRange(prim):
        total_bounds = Gf.BBox3d.Combine(
            total_bounds, Gf.BBox3d(bbox_cache.ComputeWorldBound(p).ComputeAlignedRange())
        )

    box = total_bounds.ComputeAlignedBox()

    return (box.GetMin(), box.GetMax())


def compute_bbox_size(prim: Usd.Prim) -> Tuple[float, float, float]:
    """Computes the (x, y, z) size of the axis-aligned bounding box for a prim."""
    bbox_min, bbox_max = compute_bbox(prim)
    size = (
        bbox_max[0] - bbox_min[0],
        bbox_max[1] - bbox_min[1],
        bbox_max[2] - bbox_min[2]
    )
    return size


def compute_bbox_center(prim: Usd.Prim) -> Tuple[float, float, float]:
    """Computes the (x, y, z) center of the axis-aligned bounding box for a prim."""
    bbox_min, bbox_max = compute_bbox(prim)
    center = (
        (bbox_max[0] + bbox_min[0]) / 2,
        (bbox_max[1] + bbox_min[1]) / 2,
        (bbox_max[2] + bbox_min[2]) / 2
    )
    return center


def set_visibility(prim: Usd.Prim, 
        visibility: Literal["inherited", "invisible"] = "inherited"):
    """Sets the visibility of a prim.
    
    Args:
        prim (Usd.Prim): The prim to control the visibility of.
        visibility (str):  The visibility of the prim.  "inherited" if the 
            prim is visibile as long as it's parent is visible, or invisible if 
            it's parent is invisible.  Otherwise, "invisible" if the prim is
            invisible regardless of it's parent's visibility.
    
    Returns:
        Usd.Prim: The USD prim.
    """

    attr = prim.GetAttribute("visibility")

    if attr is None:
        prim.CreateAttribute("visibility")

    attr.Set(visibility)
    return prim
    

def get_visibility(prim: Usd.Prim):
    """Returns the visibility of a given prim.
    
    See set_visibility for details.
    """
    return prim.GetAttribute("visibility").Get()
    

def rad2deg(x):
    """Convert radians to degrees."""
    return 180. * x / math.pi


def deg2rad(x):
    """Convert degrees to radians."""
    return math.pi * x / 180.


def compute_sphere_point(
        elevation: float, 
        azimuth: float, 
        distance: float
    ) -> Tuple[float, float, float]:
    """Compute a sphere point given an elevation, azimuth and distance.
    
    Args:
        elevation (float): The elevation in degrees.
        azimuth (float): The azimuth in degrees.
        distance (float): The distance.

    Returns:
        Tuple[float, float, float]: The sphere coordinate.
    """
    elevation = rad2deg(elevation)
    azimuth = rad2deg(azimuth)
    elevation = elevation
    camera_xy_distance = math.cos(elevation) * distance
    camera_x = math.cos(azimuth) * camera_xy_distance
    camera_y = math.sin(azimuth) * camera_xy_distance
    camera_z = math.sin(elevation) * distance
    eye = (
        float(camera_x), 
        float(camera_y), 
        float(camera_z)
    )
    return eye


def compute_look_at_matrix(
        at: Tuple[float, float, float], 
        up: Tuple[float, float, float], 
        eye: Tuple[float, float, float]
    ) -> np.ndarray:
    """Computes a 4x4 homogeneous "look at" transformation matrix.

    Args:
        at (Tuple[float, float, float]): The (x, y, z) location that the transform
            should be facing.  For example (0, 0, 0) if the transformation should
            face the origin.
        up (Tuple[float, float, float]):  The up axis fot the transform.  ie:
            (0, 0, 1) for the up-axis to correspond to the z-axis.
        eye (Tuple[float, float]):  The (x, y, z) location of the transform.
            For example, (100, 100, 100) if we want to place a camera at 
            (x=100,y=100,z=100)

    Returns:
        np.ndarray:  The 4x4 homogeneous transformation matrix.
    """
    at = np.array(at)
    up = np.array(up)
    up = up / np.linalg.norm(up)
    eye = np.array(eye)

    # forward axis (z)
    z_axis = np.array(eye) - np.array(at)
    z_axis = z_axis / np.linalg.norm(z_axis)

    # right axis (x)
    x_axis = np.cross(up, z_axis)
    x_axis = x_axis / np.linalg.norm(x_axis)

    # up axis
    y_axis = np.cross(z_axis, x_axis)
    y_axis = y_axis / np.linalg.norm(y_axis)
    
    matrix = np.array([
        [x_axis[0], x_axis[1], x_axis[2], 0.0],
        [y_axis[0], y_axis[1], y_axis[2], 0.0],
        [z_axis[0], z_axis[1], z_axis[2], 0.0],
        [eye[0], eye[1], eye[2], 1.0]
    ])

    return matrix
