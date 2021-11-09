from DF import dataframe
from MDF import Multilevel
from path import Path

class Open():
    def __init__(self, path, lat, lon):
        self.path = path
        self.lat = lat
        self.lon = lon
    
    def process(self):

        listd , listnd = Path.seperator(self.path)
        dff = []
        for i in listd:
            data = Multilevel(i, self.lat, self.lon).df()
            dff.extend(data)

        for i in listnd:
            data = dataframe().data()
            dff.append(data)

        return dff


