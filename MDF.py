import DF

class Multilevel():

    #PATH is the list paths
    def __init__(self, PATH, lat, lon):
        
        self.lat = lat
        self.lon = lon
        
        #this function is to get the multilevel dataframes in one unified dataframe
        self.PATH = PATH
        frames = []
        for path in self.PATH:
            df = DF.dataframe(path, self.lat, self.lon)
            frames.append(df.data())
        self.frames = frames

    def df(self):
        #to override the function data() in DF.dataframe()
        df = pd.concat(self.frames)
        return df

        



