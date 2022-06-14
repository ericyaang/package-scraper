from scraper.scraper_olx import get_infos, get_urls_df
import pandas as pd
from datetime import datetime as dt

DATA_PATH = '/data/olx_'
PAGES =  1

centro = get_urls_df('centro', PAGES)
continente = get_urls_df('continente', PAGES)
leste = get_urls_df('leste', PAGES)
norte = get_urls_df('norte', PAGES)
sul = get_urls_df('sul', PAGES)

df_all = pd.concat([centro, continente, leste, norte, sul], ignore_index=True)

infos = []
for index, row in df_all.iterrows():
    try:
        temp = get_infos(row[0], row[1], row[2], row[3], row[4])
        infos.append(temp)
    except:
        None
    print(f'Páginas registradas: {index}', end='\r')


df = pd.DataFrame(infos)
now_ = dt.now().strftime('%d%m%y-%H%M%S')
df.to_csv(DATA_PATH +
          now_ + '.csv', index=False)