import pandas as pd
import urllib.request

print('Група ФБз-01 Міщенко О.М.')
# Виведення списку адміністративних одиниць України
my_col_names=['Province', 'Адмін. одиниця']
df = pd.read_csv('province.csv', encoding = 'Windows-1251', names=my_col_names, delimiter=";", skiprows=[0])
print(df)

# Запит вводу номеру адміністративної одиниці
num=str(input('Введіть номер адмін. одиниці: '))
#Запит вводу року
year=str(input('Введіть рік: '))

# Скачування даних по url
url1='https://www.star.nesdis.noaa.gov/smcd/emb/vci/VH/get_TS_admin.php?country=UKR&provinceID='+num+'&year1='+year+'&year2='+year+'&type=Mean'
print('\nФормування посилання на завантаження:')
print(url1)
vhi_url_area = urllib.request.urlopen(url1)

#Створення csv-файлу для скачування даних
out = open('fn.csv','wb')
out.write(vhi_url_area.read())
out.close()

# Зчитати csv-файлу у фрейм, вивести імена стовпців та перший рядок:
print('\nЗавантаження текстового файлу у фрейм')
print('Імена стовпців фрейму:')
my_col_names1=['рік','тиждень', 'SMN','SMT','VCI','TCI', 'VHI']
fr = pd.read_csv('fn.csv',index_col=False, names=my_col_names1, delimiter=",", skiprows=[0,1])
print (list(fr.columns.values))
print(fr.head(52))

#пошук мінімуму VHI за рік
print('\nПошук мінімального значення VHI за '+year+' рік:')
print(fr.nsmallest(1,['VHI']))

#пошук ммаксимуму VHI за рік
print('\nПошук максимального значення VHI за '+year+' рік:')
print(fr.nlargest(1,['VHI']))

