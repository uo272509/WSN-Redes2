import requests
import time
import clr # pip install pythonnet
clr.AddReference("C:/Users/Ivan/Desktop/OpenHardwareMonitor/OpenHardwareMonitorLib.dll")
from OpenHardwareMonitor import Hardware
cp = Hardware.Computer()

cp.Open()
cp.CPUEnabled = True

def getTemps():
    [h.Update() for h in cp.get_Hardware()]
    for sens in cp.get_Hardware()[0].get_Sensors():
        if sens.get_SensorType() == Hardware.SensorType.Temperature:
            print(f"{sens.get_Name()}: {sens.get_Value()}")

def getCPUTemp():
    hw = cp.get_Hardware()[0]
    hw.Update()
    for sens in hw.get_Sensors():
        if (sens.get_Name() == "CPU Package"):
            return sens.get_Value()


#dev_id = -1

_id = requests.get("http://192.168.0.100:8000/getid")
dev_id = _id.json()["id"]

def prepareData(temp):
    return f"{dev_id}\nCPU Package,{temp}"


def sendData(data):
    print(f"Sending: {repr(data)}.")
    r = requests.post("http://192.168.0.100:8000/recieve_data", data=data)
    pass


if __name__ == "__main__":
    while(1):
        cputemp = getCPUTemp()
        print(f"CPU Package: {cputemp}")
        sendData(prepareData(cputemp))
        time.sleep(5)

        