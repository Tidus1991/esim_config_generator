#!/bin/bash
for i in {0..10}
do
   echo "========================================================\n"
   echo "This is the $i th rosbag\n"
   echo "========================================================\n"
   source ~/sim_ws/devel/setup.bash
   rosbag_num=$(printf "%09d" "$i")
   python events_contrast_maximization/tools/rosbag_to_h5.py /tmp/${rosbag_num}_out.bag --output_dir /tmp/h5_events --event_topic /cam0/events --image_topic /cam0/image_corrupted

done
