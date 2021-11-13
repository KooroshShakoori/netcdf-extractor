import DF
import pandas as pd

class Multilevel():

    #PATH is the list paths
    def __init__(self, PATH, lat, lon):
        
        self.lat = lat
        self.lon = lon
        
        #this function is designed to get the multilevel dataframes in one unified dataframe
        self.PATH = PATH

    def df(self):
        frames = []
        for path in self.PATH:
            df = DF.dataframe(path, self.lat, self.lon)
            frames.append(df.data())
        df = pd.concat(frames)
        #we can use df.shape[1] in range function
        df1 = df.set_index(pd.Index(list(range(23360))))
        return df1
