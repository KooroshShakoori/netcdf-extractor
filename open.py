import DF
import MDF
import path

class Open():
    def __init__(self, path, lat, lon):
        self.path = path
        self.lat = lat
        self.lon = lon
    
    def process(self):

        p = path.Path(self.path)    
        listd , listnd = p.seperator()
        dff = []
        for i in listd:
            M = MDF.Multilevel(i, self.lat, self.lon)
            data = M.df()
            dff.extend(data)

        for i in listnd:
            d = DF.dataframe(i, self.lat, self.lon)
            data = d.data()
            dff.append(data)

        return dff


