#!/bin/bash
rostopic pub bridge_jnt_reset edo_core_msgs/JointReset "{joints_mask: 63, disengage_steps: 2000, disengage_offset: 3.5}"
