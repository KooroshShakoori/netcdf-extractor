import open
import pandas as pd
# print(dir())

cords = [('2', 45, 17), ('3', 46, 16), ('4',46, 17)]
for i, lat, lon in cords:

    GP1 = open.Open('/mnt/h/GCM/CMIP6/CanESM5/historical/', lat, lon)
    dataframe = GP1.process()
    dataframe.to_csv(f'/mnt/c/users/gitex/desktop/data/point{i}.csv')