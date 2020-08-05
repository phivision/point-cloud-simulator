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


class SceneMaker:
    """Virtual Scene Maker"""
    def __init__(self):
        self.scene = None
        self.human = None
        self.object_list = []
        self.camera = bpy.data.objects["Camera"]
        self.light_source = None
        self.background = None

    def add_human(self, obj_path: Path):
        """Add a human model to the scene."""
        bpy.ops.import_scene.obj(filepath=str(obj_path))
        for obj in bpy.context.selected_objects:
            if obj.type == "MESH":
                obj.name = "Human"
                self.human = obj
        # debug only
        print(self.human)

    def add_object(self, obj_path: Path):
        """Add a piece of non-human object to the scene."""
        pass
