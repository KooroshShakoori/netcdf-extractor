from os import walk
import re
from pathlib import Path

#to use this module we need to make a PATH object and use the PATH.path_create to achieve the path list
#as in this moment path module is fixed and can provide expected output
class Path_generator():
    # maybe use pop() to remove 2 last part of self.path as a list and use it to create fullname
    # a function can be used to achieve this string
    def __init__(self, path):

        self.path = Path(path).resolve()
    
    def directory(self):

        directories = list(walk(self.path))[0][1]

        return directories

    def path_lists(self):
        path_nested_list = list()
        for i in self.directory():
            path_list = list()
            for file in list(walk(self.path / i))[0][2]:
                path_list.append(str(self.path / i / file))
            path_nested_list.append(path_list)

        return path_nested_list

    # def path_create(self):
    #     l1 = []
    #     l2 = []
    #     for name in self.allfiles()[0]:
    #         if bool(re.search('\d', name)):
    #             filename = re.split('\d', name)[0]
    #             fullname = f'/mnt/h/GCM/CMIP6/CanESM5/historical/{filename}/{name}'
    #             l1.append(fullname)

    #         else:
    #             filename = re.split('\\.', name)[0]
    #             fullname = f'/mnt/h/GCM/CMIP6/CanESM5/historical/{filename}/{name}'
    #             l2.append(fullname)
        

    #     return l1, l2

    # def Filter(self):
    # # Search data based on regular expression in the list
    #     mlist = []
    #     for i in self.allfiles()[1]:
    #         l = [val for val in self.path_create()[0] if re.search(i, val)]
    #         if bool(len(l) > 0):
    #             mlist.append(l)
                
    #         else:
    #             pass
        
    #     return mlist
    
    # def out(self):
    #     ld = self.Filter()
    #     lnd = self.path_create()[1]
    #     return ld , lnd


if __name__ == '__main__':
    p = Path_generator('/mnt/f/GCM/cmip6/canesm5/historical/nn/data')
    x = p.path_lists()
    print(x)
    
