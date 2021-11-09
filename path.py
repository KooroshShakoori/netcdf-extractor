from os import walk
import re

#to use this module we need to make a PATH object and use the PATH.path_create to achieve the path list

class Path():
    
    def __init__(self, path):

        self.path = path
    
    def allfiles(self):

        l1 = []
        l2 = []
        for (dirpath, dirnames, filenames) in walk(self.path):
            l1.extend(filenames)
            l2.extend(dirnames)

        return l1 , l2

    def path_create(self):
        l1 = []
        l2 = []
        for name in self.allfiles()[0]:
            if bool(re.search('\d', name)):
                filename = re.split('\d', name)[0]
                fullname = f'{filename}/{name}'
                l1.append(fullname)

            else:
                filename = re.split('\\.', name)[0]
                fullname = f'{filename}/{name}'
                l2.append(fullname)
        

        return l1, l2

    def seperator(self):

        l1 , l2 = self.path_create()
        for l in [l1, l2]:

            if bool(re.search('\d', l[0])):
                ld = []
                for i in self.allfiles()[1]:
                    matching = [s for s in l if i in s]
                    ld.append(matching)
        

            else:
                lnd = l

        return ld, lnd
