import pandas as pd

from utils.open import Open

# print(dir())

cords = [('1', 45, 16), ('2', 45, 17), ('3', 46, 16), ('4',46, 17)]
for i, lat, lon in cords:

    GP1 = Open('/mnt/f/GCM/cmip6/canesm5/ssp126/', lat, lon)
    dataframe = GP1.process()
    dataframe.to_csv(f'/mnt/c/users/gitex/desktop/data/ssps126-point{i}.csv')
    print(f'csv file for grid point{i} is made')

