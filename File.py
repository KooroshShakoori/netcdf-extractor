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
    
