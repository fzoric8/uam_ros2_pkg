import os
import xacro
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.actions import Node

def generate_launch_description():

    use_sim_time = LaunchConfiguration('use_sim_time', default='false')

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
    #xacro_ = os.path.join(get_package_share_directory('my_package_name'), xacro_file_name)
    xacro_ = os.path.join("/home/developer/ros2_ws/src/uam_ros2_pkg", xacro_file_name)
    doc = xacro.process_file(xacro_, mappings = xacro_mappings)
    robot_desc = doc.toprettyxml(indent='  ')
    params = {'robot_description': robot_desc}


    rsp = launch_ros.actions.Node(package='robot_state_publisher',
                                  node_executable='robot_state_publisher_node',
                                  output='both',
                                  parameters=[params])

    return launch.LaunchDescription([rsp])

