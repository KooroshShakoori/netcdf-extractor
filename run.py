from open import Open

GP1 = Open('/mnt/f/gcm/cmip6/canesm5/historical/nn', 45, 16)
dataframe = GP1.process()
pd.to_csv('/mnt/f/gcm/cmip6/canesm5/historical/nn/gg.csv')