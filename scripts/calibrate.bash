#!/bin/bash

master_ip="10.42.0.49"
hostname=`hostname`

export ROS_MASTER_URI=http://${master_ip}:11311
export ROS_HOSTNAME=${hostname}.local

cd ~/edo_ws
~/edo_ws/eDO_controller_v3/start.bash
source ~/edo_ws/devel/setup.bash

roslaunch edo_controller calibrate.launch