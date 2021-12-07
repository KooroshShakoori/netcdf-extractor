import DF
import MDF
import path
import pandas as pd

#variable of path in this class should be the root of all nc files
class Open():
    def __init__(self, path, lat, lon):
        self.path = path
        self.lat = lat
        self.lon = lon
    
    def process(self):

        p = path.Path_generator(self.path)    
        file_list = p.path_lists()
        mdict = dict()
        for i in file_list:
            if len(i) == 1:
                d = DF.dataframe(i, self.lat, self.lon)
                data = d.data()
                d2 = data.to_dict()
                mdict.update(d2)

            else:
                M = MDF.Multilevel(i, self.lat, self.lon)
                data = M.df()
                d1 = data.to_dict()
                mdict.update(d1)
        
        df1 = pd.DataFrame(mdict)

        return df1


