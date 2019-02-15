import csv


class RunData():
    headerData = dict()

    def __init__(self, fileName: str):
        with open(fileName, newline='') as csvfile:
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

    def getData(self):
        return self.headerData

    def getTotalDistance(self):
        totalDistance = self.headerData['distance'][-1]
        return totalDistance

    def getTotalSpeed(self):
        fastestSpeed = {'max_speed': max(self.headerData['speed'])}
        return fastestSpeed

    def getAvgSpeed(self):
        allSpeeds = {"hi": []}
        for x in self.headerData['speed']:
            allSpeeds["hi"].append(x)
        return allSpeeds
   
    def getLatLong(self):
        latLong = {"hi": []}
        for lat, lon in zip(self.headerData['lat'], self.headerData['long']):
            latLong["hi"].append((lat, lon))
        return latLong
