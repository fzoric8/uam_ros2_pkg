# uam_ros2_pkg 


ROS 2 package for the aerial manipulation.  

### Documentation: 

1. [About build system in ROS 2](https://docs.ros.org/en/foxy/Concepts/About-Build-System.html)
2. [Using URDF with robot state publisher](https://docs.ros.org/en/foxy/Tutorials/Intermediate/URDF/Using-URDF-with-Robot-State-Publisher.html)
3. [Xacro to URDF](https://gist.github.com/clalancette/5d15df1f54a1e01946659dbfa6c46c30)
4. [Official ROS 2 docs for using xacro](https://docs.ros.org/en/foxy/Tutorials/Intermediate/URDF/Using-Xacro-to-Clean-Up-a-URDF-File.html) 
5. [ament_python vs ament_cmake](https://answers.ros.org/question/342118/ament_cmake-vs-ament_python/)

## Necessary stuff

To load kopterworx, `ardupilot_gazebo` was needed, and `rapidJson`. 

[RapidJson](https://github.com/Tencent/rapidjson?tab=readme-ov-file) with installation [instructions](https://rapidjson.org/). 
[ardupilot_gazebo](https://github.com/ArduPilot/ardupilot_gazebo/tree/ros2) can be built if switched to ros2 branch. 

## PX4-SITL: 

Download following ROS package:
* [PX4-Autopilot](https://github.com/PX4/PX4-Autopilot) 

For the PX4 SITL. 

Instructions for the [PX4 cmds](https://docs.px4.io/v1.12/en/simulation/gazebo.html) in Gazebo. 

Required pip packages are: 
```
pip3 install kconfiglib
pip3 install jinja2
pip3 install future
```

## TODO: 

- [x] Build package sucessfuly
- [ ] Load UAV URDF in the ROS 2 
- [ ] Check rotor plugins for the rotors and how to add them? 
- [ ] Try to add that level of control for the Kopterworx 
- [ ] SITL for ROS 2 (Ardupilot?)

