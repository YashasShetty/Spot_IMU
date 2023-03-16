from Phidget22.PhidgetException import *
from Phidget22.Phidget import *
from Phidget22.Devices.Accelerometer import *
from Phidget22.Devices.Gyroscope import *
from Phidget22.Devices.Magnetometer import *
from Phidget22.Devices.Spatial import *
from Phidget22.Devices.TemperatureSensor import *
import traceback
import time

#Declare any event handlers here. These will be called every time the associated event occurs.

class IMU_Data:
    def __init__(self,spatial.setOnAlgorithmDataHandler(onAlgorithmData)):
        roll, pitch, yaw = spatial.setOnAlgorithmDataHandler(onAlgorithmData)
        pass
        

        
def onAccelerationChange(self, acceleration, timestamp):
    print("Acceleration: \t"+ str(acceleration[0])+ "  |  "+ str(acceleration[1])+ "  |  "+ str(acceleration[2]))
    print("Timestamp: " + str(timestamp))
    print("----------")

def onAttach(self):
    print("IMU Attached")

def onDetach(self):
    print("IMU Detached")

def onAngularRateUpdate(self, angularRate, timestamp):
    print("AngularRate: \t"+ str(angularRate[0])+ "  |  "+ str(angularRate[1])+ "  |  "+ str(angularRate[2]))
    print("Timestamp: " + str(timestamp))
    print("----------")

def onMagneticFieldChange(self, magneticField, timestamp):
    print("MagneticField: \t"+ str(magneticField[0])+ "  |  "+ str(magneticField[1])+ "  |  "+ str(magneticField[2]))
    print("Timestamp: " + str(timestamp))
    print("----------")

def onAlgorithmData(self, quaternion, timestamp):
    print("Timestamp: " + str(timestamp))

    eulerAngles = self.getEulerAngles()
    print("EulerAngles: ")
    print("\tpitch: " + str(eulerAngles.pitch))
    print("\troll: " + str(eulerAngles.roll))
    print("\theading: " + str(eulerAngles.heading))

    quaternion = self.getQuaternion()
    print("Quaternion: ")
    print("\tx: " + str(quaternion.x))
    print("\ty: " + str(quaternion.y))
    print("\tz: " + str(quaternion.z))
    print("\tw: " + str(quaternion.w))
    print("----------")

    pitch = eulerAngles.pitch
    roll = eulerAngles.roll
    yaw = eulerAngles.heading

    return roll, pitch, yaw

def onTemperatureChange(self, temperature):
    print("Temperature: " + str(temperature))

def main():
    try:
        #Create your Phidget channels
        accelerometer = Accelerometer()
        gyroscope = Gyroscope()
        magnetometer = Magnetometer()
        spatial = Spatial()
        temperatureSensor = TemperatureSensor()

        #Set addressing parameters to specify which channel to open (if any)

        #Assign any event handlers you need before calling open so that no events are missed.
        accelerometer.setOnAccelerationChangeHandler(onAccelerationChange)
        accelerometer.setOnAttachHandler(onAttach)
        accelerometer.setOnDetachHandler(onDetach)
        gyroscope.setOnAngularRateUpdateHandler(onAngularRateUpdate)
        gyroscope.setOnAttachHandler(onAttach)
        gyroscope.setOnDetachHandler(onDetach)
        magnetometer.setOnMagneticFieldChangeHandler(onMagneticFieldChange)
        magnetometer.setOnAttachHandler(onAttach)
        magnetometer.setOnDetachHandler(onDetach)
        roll, pitch, yaw = spatial.setOnAlgorithmDataHandler(onAlgorithmData)
        spatial.setOnAttachHandler(onAttach)
        spatial.setOnDetachHandler(onDetach)
        temperatureSensor.setOnTemperatureChangeHandler(onTemperatureChange)
        temperatureSensor.setOnAttachHandler(onAttach)
        temperatureSensor.setOnDetachHandler(onDetach)

        #Open your Phidgets and wait for attachment
        accelerometer.openWaitForAttachment(5000)
        gyroscope.openWaitForAttachment(5000)
        magnetometer.openWaitForAttachment(5000)
        spatial.openWaitForAttachment(5000)
        temperatureSensor.openWaitForAttachment(5000)

        #Do stuff with your Phidgets here or in your event handlers.
        spatial.setHeatingEnabled(True)

        try:
            input("Press Enter to Stop\n")
        except (Exception, KeyboardInterrupt):
            pass

        #Close your Phidgets once the program is done.
        accelerometer.close()
        gyroscope.close()
        magnetometer.close()
        spatial.close()
        temperatureSensor.close()

    except PhidgetException as ex:
        #We will catch Phidget Exceptions here, and print the error informaiton.
        traceback.print_exc()
        print("")
        print("PhidgetException " + str(ex.code) + " (" + ex.description + "): " + ex.details)


main()

