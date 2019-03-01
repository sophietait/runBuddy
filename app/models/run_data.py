import csv
from functools import reduce


class RunData:
    headerData = dict()

    def __init__(self, file_name: str):
        with open(file_name, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            headers = next(reader, None)  # this discards the header row
            for x in headers:
                self.headerData[x] = []
            for row in reader:
                self.headerData['time'].append(row[0]) # unit is seconds
                self.headerData['activityType'].append(row[1])
                self.headerData['lapNumber'].append(row[2])
                self.headerData['distance'].append(row[3]) # unit is meters
                self.headerData['speed'].append(row[4]) # unit is meters/second
                self.headerData['calories'].append(row[5])
                self.headerData['lat'].append(row[6]) 
                self.headerData['long'].append(row[7]) 
                self.headerData['elevation'].append(row[8])
                self.headerData['heartRate'].append(row[9])
                self.headerData['cycles'].append(row[10]) # unit is strides/second

    def get_data(self):
        return self.headerData

    def get_total_distance(self):
        total_distance = self.headerData['distance'][-1]
        return total_distance

    def get_total_time(self):
        total_time = self.headerData['time'][-2]
        return total_time

    def get_rate(self):
        rate = float(self.get_total_distance())/float(self.get_total_time())
        return 26.8224/rate  # converts meters per second(m/s) to minutes per mile (min/mile)

    def get_fastest_speed(self):
        fastest_speed = {'max_speed': max(self.headerData['speed'])}
        return fastest_speed

    def get_avg_speed(self):
        all_speeds = []
        for x in self.headerData['speed']:
            all_speeds.append(x)
        filtered_speeds = list(filter(None, all_speeds))
        float_speeds = list(map(lambda x: float(x), filtered_speeds))
        sum_speeds = reduce((lambda x,y: x + y), float_speeds)
        avg_speed = sum_speeds/len(float_speeds)
        return avg_speed

    def get_lat_long(self):
        lat_long = {"hi": []}
        for lat, lon in zip(self.headerData['lat'], self.headerData['long']):
            lat_long["hi"].append((lat, lon))
        return lat_long
