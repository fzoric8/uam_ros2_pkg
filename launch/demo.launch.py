import os
import xacro
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():

    use_sim_time = LaunchConfiguration('use_sim_time', default='false')

    # Model arguments
    ns = "red"
    xacro_mappings = {'namespace': ns, 
                      'enable_velodyne': False, 
                      'enable_magnet': False, 
                      'enable_gimbal': False, 
                      'enable_rotating_velodyne': False,
                      'enable_simple_manipulator': False, 
                      'fdm_port_in': None, 
                      'fdm_port_out': None, 
                      'max_range': 15, 
                      'laser_count': 16}

    xacro_file_name = 'models/kopterworx/urdf/kopterworx.urdf.xacro'
    xacro = os.path.join(
        get_package_share_directory('uam_ros2_pkg'),
        urdf_file_name)
    doc = xacro.process_file(xacro, mappings = xacro_mappings)

    rsp = launch_ros.actions.Node(package='robot_state_publisher',
                                  node_executable='robot_state_publisher_node',
                                  output='both',
                                  parameters=[params])
    robot_desc = doc.toprettyxml(indent='  ')

    return launch.LaunchDescription([rsp])



    # Robot state publisher launch

    #return LaunchDescription([
    #    DeclareLaunchArgument(
    #        'use_sim_time',
    #        default_value='false',
    #        description='Use simulation (Gazebo) clock if true'),
    #])

