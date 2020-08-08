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
Scan a virtual scene generated from the scene maker and export the point cloud.

By Fanghao Yang, 08/01/2020
"""
import click
from lidar_sim_lib.scene_maker import SceneMaker
from pathlib import Path

# debug helper
# import ptvsd
# host = "localhost"
# port = 5678
# ptvsd.enable_attach(address=(host, port), redirect_output=True)
# ptvsd.wait_for_attach()


@click.command()
@click.option('--human', help="Input directory contains a list of obj files to scan")
@click.option('--output', help="Output directory for exporting a list of scanned point clouds")
def batch_scan(human: str, output: str):
    """Batch scan all obj files in a directory

    Args:
        input (str): Input directory for obj files
        output (str): Output directory for pcd files
    """
    human_path = Path(human)
    output_path = Path(output)
    human_obj_list = []
    human_obj_list.extend(human_path.glob("*.obj"))
    if human_obj_list:
        for human_obj in human_obj_list:
            new_scene_maker = SceneMaker()
            new_scene_maker.add_human(human_obj)
            pcd_path = output_path.joinpath(human_obj.stem+'.pcd')
            new_scene_maker.export_point_cloud(pcd_path)
    else:
        raise OSError("Can't find valid obj files in the given path")
    
if __name__ == '__main__':
    batch_scan()