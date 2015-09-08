#!/usr/bin/python
# -*- coding: utf-8 -*-

from geometry_msgs.msg import Point
import rospy
import sys

pos_person_nearest = Point()

def cb_find_person(person):
   pos_person_nearest = person.people.pos

if __name__=='__main__':
    ####
    # Recognize a human's face and bring over the bottle to him.
    ####
    
    # Lift up the torso to look for human's faces.
    whole_body.move_to_joint_positions({'arm_lift_joint': 0.3})
    ##whole_body.move_to_joint_positions({'head_tilt_joint': 0.3})
    
    # eef down to clear the eyesight
    whole_body.move_to_joint_positions({'arm_flex_joint': -1.57})
    
    # Look right 90 deg to find the nearest human's face.
    whole_body.move_to_joint_positions({'head_pan_joint': -1.57})
    
    rospy.Subscriber("/face_detector/people_tracker_measurements_array", PositionMeasurementArray, cb_find_person)

    pose_person = geometry.pose(x=pos_person_nearest.x, y=pos_person_nearest.y)
    whole_body.move_end_effector_pose(pose_person)
