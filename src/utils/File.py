from netCDF4 import Dataset as nc

class Read():

    '''
    this class is designed to read the nc file
    '''
    def __init__(self, path):
       
        #we treat the netCDF4.Dataset as a file
        self.path = path
        self.file = nc(self.path, mode='r')
        self.name = self.file.variable_id
    
if __name__ == '__main__':
    F = Read('/mnt/f/GCM/cmip6/canesm5/historical/nn/data/hus/hus2.nc')
    print(F.file['hus'][:, 1, 10, 11])
    print(F.name)
