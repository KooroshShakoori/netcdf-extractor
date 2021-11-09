from File import Read
import pandas as pd

class dataframe(Read):

    def __init__(self, path, lat, lon):
        super.__init__(path)
        #lat and lon have to be in index format 
        self.lat = lat
        self.lon = lon

    def data(self):

        #the conditional statement below is for deviding the files with and without plev variable
        if len(self.file.dimensions) == 4:
            data = list(self.file[self.name][:, self.lat, self.lon])[-23360:]
            df = pd.DataFrame(data, columns=self.name)
            return df

        else:
            l1 = list()
            l2 = list(range(7))
            for i in l2:

                data = self.file[self.name][:, i, self.lat, self.lon]
                l1.append(list(data))
            d1 = dict(list(f'{self.name}{i}'for i in l2) , l1)
            df = pd.DataFrame(d1)
            return df


        