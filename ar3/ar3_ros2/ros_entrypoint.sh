#!/bin/bash
set -e

if [ $ROS_DISTRO == "noetic" ]; then
    echo "noetic ros_entrypoint ..."
    source "/opt/ros/$ROS_DISTRO/setup.bash"
    . /usr/share/gazebo/setup.sh
else
    echo "other ros2 ros_entrypoint..."
    source "/opt/ros/$ROS_DISTRO/setup.bash"
    # source /app/colcon_ws/install/setup.bash
    . /usr/share/gazebo/setup.sh
    # export TURTLEBOT3_MODEL=waffle
    #export XDG_RUNTIME_DIR=/app/cache
    #export RMW_IMPLEMENTATION=rmw_cyclonedds_cpp
    #export CYCLONEDDS_URI=file:///app/cyclonedds.xml
fi

exec "$@"


