import open
import pandas as pd
# print(dir())



GP1 = open.Open('/mnt/f/gcm/cmip6/canesm5/historical/nn/data/', 45, 16)
dataframe = GP1.process()
dataframe.to_csv('/mnt/f/gcm/cmip6/canesm5/historical/nn/gg.csv')