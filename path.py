from os import walk
import re

#to use this module we need to make a PATH object and use the PATH.path_create to achieve the path list
#as in this moment path module is fixed and can provide expected output
class Path():
    # maybe use pop() to remove 2 last part of self.path as a list and use it to create fullname
    # a function can be used to achieve this string
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
                fullname = f'/mnt/f/GCM/cmip6/canesm5/historical/nn/data/{filename}/{name}'
                l1.append(fullname)

            else:
                filename = re.split('\\.', name)[0]
                fullname = f'/mnt/f/GCM/cmip6/canesm5/historical/nn/data/{filename}/{name}'
                l2.append(fullname)
        

        return l1, l2

    def Filter(self):
    # Search data based on regular expression in the list
        mlist = []
        for i in self.allfiles()[1]:
            l = [val for val in self.path_create()[0] if re.search(i, val)]
            if bool(len(l) > 0):
                mlist.append(l)
                
            else:
                pass
        
        return mlist
    
    def out(self):
        ld = self.Filter()
        lnd = self.path_create()[1]
        return ld , lnd


if __name__ == '__main__':
    p = Path('/mnt/f/GCM/cmip6/canesm5/historical/nn/data')
    x, y = p.out()
    print(x)
    print(y)
