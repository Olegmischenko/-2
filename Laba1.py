import pandas as pd
import urllib.request
from datetime import datetime as DT
import numpy as np

print('Група ФБз-01 Міщенко О.М.')
# Виведення списку адміністративних одиниць України
my_col_names=['Province', 'Адмін. одиниця']
df = pd.read_csv('province.csv', encoding = 'Windows-1251', names=my_col_names, delimiter=";", skiprows=[0])
print(df)

# Запит вводу номеру адміністративної одиниці
num=str(input('Введіть номер адмін. одиниці: '))

# Скачування даних по url
url1='https://www.star.nesdis.noaa.gov/smcd/emb/vci/VH/get_TS_admin.php?country=UKR&provinceID='+num+'&year1=1981&year2=2022&type=Mean'
print('\nФормування посилання на завантаження:')
print(url1)
vhi_url_area = urllib.request.urlopen(url1)
out = open('file_name','wb')
file_name = f'vhi_id_num_{DT.now():%Y-%m-%d_%H-%M}.csv'
out.write(vhi_url_area.read())
out.close()
print('\nНазва файлу з датою та часом завантаження: '+file_name)

# Зчитати csv-файлу у фрейм, вивести імена стовпців та перший рядок:
print('Завантаження текстового файлу у фрейм')
print('\nІмена стовпців фрейму:')
my_col_names1=['рік','тиждень', 'SMN','SMT','VCI','TCI', 'VHI']
fr = pd.read_csv('file_name',index_col=False, names=my_col_names1, delimiter=",", skiprows=[0,1])
print (list(fr.columns.values))
print('Друк перших 20 строк для прикладу:')
print (fr[:20])

#Сортування датафрейму:
print('\nСортування датафрейму: ')
sorted_province=pd.DataFrame(np.sort(df,axis=0), columns=df.columns)
print (sorted_province['Адмін. одиниця'].tail(26))