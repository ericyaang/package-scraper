from bs4 import BeautifulSoup
import requests
import pandas as pd
from datetime import datetime as dt
from IPython.display import clear_output
from scraper import get_urls, get_infos, get_urls_df

DATA_PATH = './data'

##
# Part 1
##
centro = get_urls_df('centro')
continente = get_urls_df('continente')
leste = get_urls_df('leste')
norte = get_urls_df('norte')
sul = get_urls_df('sul')

df_all = pd.concat([centro, continente, leste, norte, sul], ignore_index=True)

##
# Part 2
##
start_time = dt.now()

infos = []
for index, row in df_all.iterrows():
    try:
        temp = get_infos(row[0], row[1], row[2], row[3], row[4])
        infos.append(temp)
    except:
        None
    print(f'Páginas registradas: {index}', end='\r')

time_elapsed = (dt.now() - start_time)
print(f'Duração: {time_elapsed}')


# create df and save
df = pd.DataFrame(infos)
now_ = dt.now().strftime('%d%m%y-%H%M%S')
df.to_csv(DATA_PATH +
          now_ + '.csv', index=False)
