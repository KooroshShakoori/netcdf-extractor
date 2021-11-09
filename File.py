from netCDF4 import Dataset as nc

class read():

    '''
    this class is designed to read the nc file
    '''
    def __init__(self, path):
       
        #we treat the netCDF4.Dataset as a file
        self.file = nc(path, mode='r')
        self.name = self.file.variable_id
    
