from waggle.data.measurements import MeasurementsFile
from waggle.plugin import Plugin
import io
import pandas as pd
import time

debug = False

def publishData(plugin, msg, data):
    site = "SITEX"
    values = data.split(',')
    timestamp = int(pd.to_datetime(values[0], unit="s").value)
    meta = {"wsnid": values[1], "siteid": site, "sensor": "wsn" + values[1]}
    plugin.publish("wsn.sap_flow_density", float(values[2]), timestamp=timestamp, meta=meta)
    plugin.publish("wsn.stem_humidity", float(values[3]), timestamp=timestamp, meta=meta)
    plugin.publish("wsn.radial_growth", float(values[4]), timestamp=timestamp, meta=meta)
    plugin.publish("wsn.ndvi", float(values[5]), timestamp=timestamp, meta=meta)
    plugin.publish("wsn.green_red", float(values[6]), timestamp=timestamp, meta=meta)
    plugin.publish("wsn.leaf_temperature", float(values[7]), timestamp=timestamp, meta=meta)
    plugin.publish("wsn.air_temperature", float(values[8]), timestamp=timestamp, meta=meta)
    plugin.publish("wsn.rel_air_humidity", int(float(values[9])), timestamp=timestamp, meta=meta)
    plugin.publish("wsn.gas_co2", int(float(values[10])), timestamp=timestamp, meta=meta)
    plugin.publish("wsn.gas_o3", int(float(values[11])), timestamp=timestamp, meta=meta)
    plugin.publish("wsn.gas_pm2.5", int(float(values[12])), timestamp=timestamp, meta=meta)
    plugin.publish("wsn.gas_pm10", int(float(values[13])), timestamp=timestamp, meta=meta)
    plugin.publish("wsn.flame_pulses", int(float(values[14])), timestamp=timestamp, meta=meta)
    plugin.publish("wsn.flame_flag", int(float(values[15])), timestamp=timestamp, meta=meta)
    plugin.publish("wsn.trunk_axis_movement", float(values[16]), timestamp=timestamp, meta=meta)
    plugin.publish("wsn.risk_index", round(float(values[17]), 1), timestamp=timestamp, meta=meta)
    print("Plugin published:", msg)


def main():
    if debug is True:
        sensor = MeasurementsFile(filename="test-run/data.ndjson")
        data = sensor.play()
        with Plugin() as plugin:
            for msg in data:
                publishData(plugin, msg, msg["value"])

    else:
        inc = 0
        with Plugin() as plugin:
            plugin.subscribe("wsn.input")
            print("Subscribed to wsn.input", flush=True)
            while True:
                msg = plugin.get()
                publishData(plugin, msg, msg.value)
                inc = inc + 1
                if inc == 30:
                    break


if __name__ == "__main__":
    main()
