from lidar_sim_lib.scene_maker import SceneMaker
from pathlib import Path
# debug helper
# import ptvsd
# host = "localhost"
# port = 5678
# ptvsd.enable_attach(address=(host, port), redirect_output=True)
# ptvsd.wait_for_attach()


def run_lidar_sim():
    """Run the lidar simulation script."""
    human_model_path = Path("/home/fanghao/3d_models/skp_model_output/Bathman01.obj")
    maker = SceneMaker()
    maker.add_human(human_model_path)
    export_pcd_path = Path("/home/fanghao/Documents/test.pcd")
    maker.export_point_cloud(export_pcd_path)
    # test and debug
    print("Point cloud exported!")
    

if __name__ == "__main__":
    """
    This is a experimental code to generate lidar simulation data
    automatically with Python virtual operator.
    When exit Blender headless version, there might be some unfreed 
    memory blocks, which is low level bug in Blender.
    """
    run_lidar_sim()
    