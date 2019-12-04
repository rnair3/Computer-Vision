import requests
import os
import pandas as pd

df = pd.read_excel('Product_Sheet.xlsx')

if 'data' not in os.listdir():
    os.mkdir('data')

for url in df.prd_image.values:
    res = requests.get(url)
    with open(os.path.join('data', url.split('/')[-1]), 'wb') as f:
        f.write(res.content)