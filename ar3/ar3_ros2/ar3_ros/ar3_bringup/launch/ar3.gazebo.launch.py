# Copyright 2021 Open Source Robotics Foundation, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, SetEnvironmentVariable
from launch.substitutions import LaunchConfiguration, Command, FindExecutable, PathJoinSubstitution
from launch.launch_description_sources import PythonLaunchDescriptionSource

from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare
from launch.actions import DeclareLaunchArgument, ExecuteProcess


import os
import yaml, xacro
from ament_index_python.packages import get_package_share_directory, get_package_prefix

def generate_launch_description():

    # gazebo = IncludeLaunchDescription(
    #     PythonLaunchDescriptionSource(
    #         [PathJoinSubstitution([FindPackageShare("gazebo_ros"), "launch", "gazebo.launch.py"])]
    #     ),
    #     launch_arguments={"verbose": "false"}.items(),
    # )

    world = os.path.join(get_package_share_directory("ar3_description"), "worlds", "empty.world")
    description_share = os.path.join(get_package_prefix('ar3_description'), 'share')
    env_var = SetEnvironmentVariable('GAZEBO_MODEL_PATH', description_share)  

    gazebo_server = ExecuteProcess(
        cmd=[
            "gzserver",
            "--verbose",
            "-u",
            "-s", "libgazebo_ros_factory.so",
            "-s", "libgazebo_ros_init.so",
            world,
        ],
        output="screen",)
    gazebo_client = ExecuteProcess(cmd=["gzclient"], output="screen")

    robot_spawn_entity = Node(
        package="gazebo_ros",
        executable="spawn_entity.py",
        arguments=[
            "-topic", "/robot_description",
            "-entity", "ar3_robot",
            "-x", "0.0",
            "-y", "0.0",
            "-z", "0.0",
            "-Y", "0.0",
            "-unpause",
        ],
        output="screen",)

    # Get URDF via xacro
    robot_description_content = Command(
        [
            PathJoinSubstitution([FindExecutable(name="xacro")]),
            " ",
            PathJoinSubstitution(
                [
                    FindPackageShare("ar3_description"),
                    "urdf",
                    "ar3.urdf.xacro",
                ]
            ),
            " sim_gazebo:=true",
        ]
    )
    robot_description = {"robot_description": robot_description_content}

    node_robot_state_publisher = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        output="screen",
        parameters=[robot_description],
    )

    spawn_broadcaster = ExecuteProcess(
        cmd=["ros2 run controller_manager spawner {}".format("joint_state_broadcaster")],
        shell=True,
        output="screen",)
    
    spawn_controller = ExecuteProcess(
        cmd=["ros2 run controller_manager spawner {}".format("ar3_controller")],
        shell=True,
        output="screen",)

    return LaunchDescription(
        [
            env_var, 
            gazebo_server, 
            gazebo_client,    
            # gazebo,
            node_robot_state_publisher,
            robot_spawn_entity,
            spawn_broadcaster,
            spawn_controller,
            
        ]
    )

























    # spawn_controller = Node(
    #     package="controller_manager",
    #     executable="spawner",
    #     arguments=["joint_state_broadcaster", "--controller-manager", "/controller_manager"],
    # ) 
    # Node(
    #     package="controller_manager",
    #     executable="spawner",
    #     arguments=["joint_state_broadcaster"],
    #     output="screen",
    # )