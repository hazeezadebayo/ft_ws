FT-Sensor and ROS control behavior test 
===============================

arbitrary robot arm model name chosen coincidentally AR3. urdf describes a 2-jointed robotic arm provided in both ROS1 and ROS2 Packages. docker files were provided for ease of reproducibility. The observed problem is that gazebo `<plugin filename="libgazebo_ros_control.so" name="control"/>` has different behaviors for both ros1 and ros2. This implementation leads to discrepancies in the published `force-torque` wrench values given any joint command. When this plugin is removed, wrench values published in both ros1 and ros2 are similar/same.





Usage:

==========
- ROS1 Build
==========
TERMINAL 1:
```bash
$ cd ft_ws/ar3/ar3_ros1
$ export DISPLAY=:1.0 && xhost +local:docker && docker-compose up --build
```

TERMINAL 2:
```bash
$ docker system prune && docker exec -it ar3_ros1_ros_noetic_1 bash
# $ rostopic type /ar3_controller/command --> trajectory_msgs/JointTrajectory
$ rostopic pub /ar3_controller/command trajectory_msgs/JointTrajectory '{joint_names: ["joint1","joint2"], points: [{positions:[0,1.0],velocities:[0,0.001],time_from_start: [3,0]}]}' -1
# $ gz topic -view /gazebo/default/ar3_robot/joint2/force_torque/wrench
```

TERMINAL 3:
```bash
$ docker system prune && docker exec -it ar3_ros1_ros_noetic_1 bash
$ rostopic echo /joint_states
```

TERMINAL 4:
```bash
$ docker system prune && docker exec -it ar3_ros1_ros_noetic_1 bash
$ rostopic echo /ft_sensor_j2
```

==========
- ROS2 Build
==========

TERMINAL 1:
```bash
$ cd ft_ws/ar3/ar3_ros2
$ export DISPLAY=:1.0 && xhost +local:docker && docker-compose up --build
```

TERMINAL 2:
```bash
$ docker system prune && docker exec -it ar3_ros2_ros_humble_1 bash
# $ ros2 topic type /ar3_controller/joint_trajectory --> trajectory_msgs/msg/JointTrajectory
$ ros2 topic pub --once /ar3_controller/joint_trajectory trajectory_msgs/JointTrajectory "{header: {stamp: {sec: 0, nanosec: 0}, frame_id: ''}, joint_names: ['joint1', 'joint2'], points: [{positions: [0.0, 1.0], velocities: [0.0, 0.001], time_from_start: {sec: 3, nanosec: 0}}]}"
# $ gz topic -view /gazebo/default/ar3_robot/joint2/force_torqueX/wrench
```

TERMINAL 3:
```bash
$ docker system prune && docker exec -it ar3_ros2_ros_humble_1 bash
$ ros2 topic echo /joint_states
```

TERMINAL 4:
```bash
$ docker system prune && docker exec -it ar3_ros2_ros_humble_1 bash
$ ros2 topic echo /ft_sensor_j2
```










===============================
# unnecessary but...
## Simple simulation of AR3
The `use_fake_hardware` flag uses a simple software loop back, which won't
communicate with the real AR3 robot arm.
ros2 launch ar3_bringup ar3_base.launch.py use_fake_hardware:=True
sudo docker cp ar3_ros_noetic_1:/app/world_simple ~/Desktop/