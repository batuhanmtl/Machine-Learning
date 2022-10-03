import pandas as pd

df = pd.read_excel(r'https://www.dropbox.com/s/luoopt5biecb04g/SATILIK_EVxlsx?dl=1')

df.drop('Unnamed: 0',inplace=True,axis=1)

df.columns= ['price','rooms','m2','floor','age']

df.to_csv('real_estate')

print(1e-15)
1e10
1e-8
1e-4
1e-3
1e-2
1e-15
1e-15

