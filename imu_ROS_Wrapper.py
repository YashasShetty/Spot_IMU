import rospy
from IMU_driver import IMU_Data


class IMU_data_wrapper:
    def __init__(self):
        self.send_IMU_data = rospy.Publisher('IMU_Data', float, queue_size=10)
        self.get_IMU_data = IMU_Data()

    def publish_roll(self):
        roll = self.get_IMU_data.roll
        self.send_IMU_data.publish(roll)
        print("roll ",roll )
    def publish_pitch(self):
        pitch = self.get_IMU_data.pitch
        self.send_IMU_data.publish(pitch)
        print("pitch ",pitch)
    def publish_yaw(self):
        yaw = self.get_IMU_data.yaw
        self.send_IMU_data.publish(yaw)
        print("yaw ",yaw)

if __name__ == "__main__":
    rospy.init_node("IMU_driver")
    angles = IMU_data_wrapper()
    angles.publish_current_data()
    rospy.on_shutdown(angles.stop)

    rospy.loginfo("Motor driver is now started, ready to get commands.")

    rospy.loginfo(angles)