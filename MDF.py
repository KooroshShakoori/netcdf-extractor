from DF import dataframe

class Multilevel(dataframe):

    #PATH is the list paths
    def __init__(self, PATH, lat, lon):
        
        #this function is to get the multilevel dataframes in one unified dataframe
        self.PATH = PATH
        frames = []
        for path in self.PATH:
            super().__init__(self, path, lat, lon)
            frames.append(self.data())
        self.frames = frames

    def df(self):
        #to override the function data() in DF.dataframe()
        df = pd.concat(self.frames)
        return df

        



