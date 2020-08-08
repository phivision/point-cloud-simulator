# Phi Vision, Inc.
# __________________

# [2020] Phi Vision, Inc.  All Rights Reserved.

# NOTICE:  All information contained herein is, and remains
# the property of Phi Vision Incorporated and its suppliers,
# if any.  The intellectual and technical concepts contained
# herein are proprietary to Phi Vision, Inc
# and its suppliers and may be covered by U.S. and Foreign Patents,
# patents in process, and are protected by trade secret or copyright law.
# Dissemination of this information or reproduction of this material
# is strictly forbidden unless prior written permission is obtained
# from Phi Vision, Inc.

"""
Make a virtual scene from existing model list

By Fanghao Yang, 08/01/2020
"""

import bpy
from pathlib import Path
# global variables
SENSOR_TYPE = "tof"
SENSOR_X_RES = 512
SENSOR_Y_RES = 384
SENSOR_FOV = 58.986
SENSOR_ASPECT_RATIO = 4.0/3.0


class SceneMaker:
    """Virtual Scene Maker"""
    def __init__(self):
        self.scene = bpy.context.scene
        self.human = None
        self.object_list = []
        # delete default mesh with starting
        for o in bpy.context.scene.objects:
            if o.type == 'MESH':
                o.select = True
            else:
                o.select = False
        bpy.ops.object.delete()
        self.camera = bpy.data.objects["Camera"]
        # default setting of lidar sensor
        self.camera.scan_type = SENSOR_TYPE
        self.camera.tof_xres = SENSOR_X_RES
        self.camera.tof_yres = SENSOR_Y_RES
        self.camera.add_scan_mesh = False
        self.camera.store_data_in_mesh = False
        self.camera.save_scan = True
        self.camera.show_in_frame = True
        self.camera.tof_lens_angle_w = SENSOR_FOV
        self.camera.tof_lens_angle_h = SENSOR_FOV / SENSOR_ASPECT_RATIO
        # default setting of light source
        self.light_source = bpy.data.objects["Lamp"]
        self.background = None

    def __del__(self):
        """Delete all meshes when delete the scene maker
        """
        for o in bpy.context.scene.objects:
            if o.type == 'MESH':
                o.select = True
                bpy.ops.object.delete()
        
    def export_point_cloud(self, pc_path: Path):
        """Export scan as point cloud

        Args:
            pc_path: point cloud export path

        Returns:

        """
        bpy.ops.blensor.scan(filepath=str(pc_path))

    def add_human(self, obj_path: Path):
        """Add a human model to the scene.

        Args:
            obj_path: obj file of human model

        """
        bpy.ops.import_scene.obj(filepath=str(obj_path))
        for obj in bpy.context.selected_objects:
            if obj.type == "MESH":
                obj.name = "Human"
                self.human = obj
        # debug only
        print(self.human.type)

    def add_object(self, obj_path: Path):
        """Add a piece of non-human object to the scene."""
        pass
