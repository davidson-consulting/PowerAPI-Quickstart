from datetime import datetime
import copy
import sys
import os
import json 
from influxdb import InfluxDBClient

def getEnergyConsumption(start, end):
    print(f"Should get the energy consumption between {datetime.fromtimestamp(start)} and {datetime.fromtimestamp(end)}")
    client = InfluxDBClient(host='localhost', port=8086)
    client.switch_database('powerapi_formula')
    rawDataPower = client.query(f'''
            SELECT target, mean, median, stddev 
            FROM (select mean(power), median(power), stddev(power) FROM "power_consumption" where time > {start}s and time < {end}s GROUP BY "target")
        '''
        , epoch='s')
    results = []
    try:
        for result in rawDataPower.get_points():
            meanPowerConsumption = result['mean']
            medianPowerConsumption = result['median']
            stddevPowerConsumption = result['stddev']
            target = result['target']

            rawDataPower = client.query(f'SELECT power from "power_consumption" where time > {start}s and time < {end}s and ("target" = \'{target}\')', epoch='s')
            powerConsumption = list(map(lambda e: e['power'], list(rawDataPower.get_points())))
            print(f"Energy consummed ({target}): MEAN {meanPowerConsumption} - MEDIAN {medianPowerConsumption} - STDDEV {stddevPowerConsumption}")
            results.append({"meanPowerConsumption": meanPowerConsumption, 
                    "medianPowerConsumption": medianPowerConsumption, 
                    "stddevPowerConsumption": stddevPowerConsumption,
                    "powerConsumption": powerConsumption,
                    "target": target})
        return results
    except StopIteration:
        print(f"Could not get energy consumption between {datetime.fromtimestamp(start)} and {datetime.fromtimestamp(end)} - PASS")
        return {}

def main(args):
    if len(args) < 2:
        print("Usage : python analysis.py START END")
        return 1
    
    json.dumps(getEnergyConsumption(int(args[1]), int(args[2])))

if __name__ == "__main__":
    main(sys.argv)