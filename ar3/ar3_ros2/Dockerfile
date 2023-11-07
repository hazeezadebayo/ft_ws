ARG ROS_DISTRO=humble


FROM osrf/ros:$ROS_DISTRO-desktop


SHELL ["/bin/bash", "-c"]


# setup environment
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV ROS_DISTRO $ROS_DISTRO


# Check the value of ROS_DISTRO
RUN if [ "$ROS_DISTRO" = "noetic" ]; then \
        echo "noetic...ROS1"; \
        # Install project's ROS1 deppendencies
        sudo apt update && \
        sudo apt install -y \
        ros-$ROS_DISTRO-soem \
        ros-$ROS_DISTRO-moveit* \
        ros-$ROS_DISTRO-gazebo* \
        ros-$ROS_DISTRO-robot-* \
        ros-$ROS_DISTRO-joint-* \
        ros-$ROS_DISTRO-rqt* \
        ros-$ROS_DISTRO-kdl* \
        ros-$ROS_DISTRO-control-* \
        ros-$ROS_DISTRO-controller* \
        ros-$ROS_DISTRO-plotjuggler* \
        ros-$ROS_DISTRO-industrial-* \
        ros-$ROS_DISTRO-trac-ik* \
        ros-$ROS_DISTRO-trajectory* \
        ros-$ROS_DISTRO-transmission* \
        ros-$ROS_DISTRO-scaled* \
        ros-$ROS_DISTRO-ur-* \
        ros-$ROS_DISTRO-pass-through-controllers* \
        ros-$ROS_DISTRO-rosbridge-suite \
        ros-$ROS_DISTRO-xacro \
        ros-$ROS_DISTRO-tf2-ros \
        ros-$ROS_DISTRO-rviz \
        ros-$ROS_DISTRO-cv-bridge \
        ros-$ROS_DISTRO-actionlib \
        ros-$ROS_DISTRO-actionlib-msgs \
        ros-$ROS_DISTRO-dynamic-reconfigure \
        ros-$ROS_DISTRO-trajectory-msgs \
        ros-$ROS_DISTRO-octomap-rviz-plugins \
        ros-$ROS_DISTRO-catkin \
        ros-$ROS_DISTRO-rospy-message-converter \
        ros-$ROS_DISTRO-realtime-tools \
        ros-$ROS_DISTRO-ros-controllers \
        ros-$ROS_DISTRO-tf-conversions \
        ros-$ROS_DISTRO-kdl-parser \
        ros-$ROS_DISTRO-ros-control \
        ros-$ROS_DISTRO-ros-controllers \
        ros-$ROS_DISTRO-robot-localization \
        ros-$ROS_DISTRO-tf2-msgs \
        ros-$ROS_DISTRO-libg2o \
        ros-$ROS_DISTRO-twist-mux && \
        sudo apt-get install -y python3-catkin-tools && \
        sudo rm -rf /var/lib/apt/lists/*; \
    else \
        echo "others...ROS2"; \
        sudo apt update && \
        sudo apt install -y \
        ros-$ROS_DISTRO-diagnostic-updater \
        ros-$ROS_DISTRO-geographic-msgs \
        ros-$ROS_DISTRO-moveit* \
        ros-$ROS_DISTRO-gazebo* \
        ros-$ROS_DISTRO-robot-* \
        ros-$ROS_DISTRO-joint-* \
        ros-$ROS_DISTRO-xacro \
        ros-$ROS_DISTRO-robot-localization \
        ros-$ROS_DISTRO-kdl-parser* \
        ros-$ROS_DISTRO-tf2-msgs \
        ros-$ROS_DISTRO-test-msgs \
        ros-$ROS_DISTRO-libg2o \
        ros-$ROS_DISTRO-realtime-tools \
        ros-$ROS_DISTRO-ros2-control \
        ros-$ROS_DISTRO-ros2-controllers \
        ros-$ROS_DISTRO-control-* \
        ros-$ROS_DISTRO-controller* \
        ros-$ROS_DISTRO-plotjuggler* \
        ros-$ROS_DISTRO-twist-mux \
        ros-$ROS_DISTRO-rmw-cyclonedds-cpp \
        ros-$ROS_DISTRO-rmw-fastrtps-* && \
        sudo rm -rf /var/lib/apt/lists/*; \
    fi


# Install project's python deppendencies
RUN sudo apt-get update  && \
    sudo apt-get install -y software-properties-common && \
    sudo apt-get update  && \
    sudo add-apt-repository universe && \
    sudo apt-get update  && \
    sudo apt-get install -y pyqt5-dev-tools && \
    sudo apt-get update  && \
    sudo apt-get install -y mlocate && \
    sudo apt-get update  && \ 
    sudo apt-get install -y \
            python3-osrf-pycommon \
            build-essential \
            nano \
            tmux \
            git \
            liborocos-kdl* \
            libkdl* \
        build-essential \
        cmake \
        libboost-all-dev \
        libxml-xpath-perl \
        libboost-all-dev \
        pkg-config \
        libxml2-dev \
        ruby-dev \
        python3-dev \
        python3-wstool \
        python3-vcstools \
        python3-rosdep \
        python3-pandas \
        python3-opencv \
	    python3-pip && \
    sudo apt-get update  && \
    pip3 install \
        pyrealsense2 \
        python-snap7 \
        APScheduler && \
    sudo apt-get update  && \
    pip3 install twilio && \
    sudo apt install -y \
        net-tools \
        nginx \
        libeigen3-dev \
        libcppunit-dev \
        doxygen \
        graphviz \
#        gazebo \
        libnlopt* && \
    sudo apt-get update && \
    sudo rm -rf /var/lib/apt/lists/*

# sudo apt install libignition-gazebo-dev ignition-tools


# clean all install related cache
RUN sudo apt autoremove && \
    sudo apt autoclean && \
    sudo apt upgrade && \
    sudo apt update && \
    sudo rm -rf /var/lib/apt/lists/*


# Source the ROS environment setup script
RUN echo ". /opt/ros/$ROS_DISTRO/setup.bash" >> ~/.bashrc 

WORKDIR /app 

COPY ar3/ar3_ros2/ar3_ros ar3_ros/

COPY ar3/ar3_ros2/ros_entrypoint.sh /

RUN chmod +x /ros_entrypoint.sh


ENTRYPOINT ["/ros_entrypoint.sh"]   
CMD ["bash"]





