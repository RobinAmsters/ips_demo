#!/usr/bin/env python

import rospy
import tf

from marvelmind_nav.msg import hedge_pos

def callback(hedge_pos):
    frame_pub.sendTransform((hedge_pos.x_m, hedge_pos.y_m, hedge_pos.z_m), tf.transformations.quaternion_from_euler(0.0, 0.0, 0.0), rospy.Time.now(), "marvelmind", "odom")

rospy.init_node('marvelmind_tf', anonymous=True)
hedge_sub = rospy.Subscriber('/hedge_pos', hedge_pos, callback)
frame_pub = tf.TransformBroadcaster()

rospy.spin()


