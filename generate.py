import numpy as np
import time
from waggle.plugin import Plugin

from datetime import datetime

id = "543200"

sampleData = [
    "0.9494,18.8267,1.7749,0.3768,0.4499,24.4524,11.0,101.0,1230.0,69.9697,1.0,3.0,0.0,0.0,0.0,4.1989,8.9999,39.03333,0.1327",
    "0.0,48.1033,9.9317,0.0,0.2214,13.2619,7.2,87.0,1126.25,67.8808,1.0,2.0,0.0,0.0,0.0,6.5713,8.9999,15.6191,0.2831",
    "5.684341886080802e-14,27.2886,286.9198,0.0696,0.1829,13.5524,13.8,53.0,1855.0,66.7171,1.0,2.0,0.0,0.0,0.0,6.6873,8.2946,14.7095,0.1541",
]


def publishSample(plugin, counter):
    timestamp = time.time()
    for i in range(30):
        index = (counter + i) % len(sampleData)
        data = str(int(time.time())) + "," + id + str(i).zfill(2) + "," + sampleData[index]
        plugin.publish("wsn.input", data, timestamp=time.time_ns(), scope="node")
    return None


def main():
    counter = 0
    with Plugin() as plugin:
        while True:
            publishSample(plugin, counter)
            counter = counter + 1
            if counter == 1:
                break
            time.sleep(30)


if __name__ == "__main__":
    main()
