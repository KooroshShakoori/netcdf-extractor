from src.utils.Files import Read

import pandas as pd

class dataframe(Read):

    def __init__(self, path, lat, lon):
        super().__init__(path)
        #lat and lon have to be in index format 
        self.lat = lat
        self.lon = lon

    def data(self):

        #the conditional statement below is for deviding the files with and without plev variable(4 is for files without a plev value)(probably will cause inconsistency 
        #with multiple filed variable without a plev like ncep files)---> therefore needs to be redesigned
        if len(self.file.dimensions) == 4:
            data = list(self.file[self.name][:, self.lat, self.lon])
            df = pd.DataFrame({self.name : data})
            return df

        else:
            l1 = list()
            l2 = list(range(8))
            l3 = [f'{self.name}{i}' for i in l2]
            for i in l2:

                data = self.file[self.name][:, i, self.lat, self.lon]
                l1.append(list(data))
            d1 = dict(zip(l3, l1))
            df = pd.DataFrame(d1)
            return df

if __name__ == '__main__':
    d = dataframe('/mnt/f/GCM/cmip6/canesm5/historical/nn/data/hus/hus1.nc', 16, 19)
    data = d.data()
    print(data)
