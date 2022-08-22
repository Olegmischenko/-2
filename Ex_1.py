#encodings='windows-1251'
# tested with python3.9
import json
import urllib.request
from spyre import server
from googlefinance.client import get_price_data

server.include_df_index = True

class StockExample(server.App):
    title = "Аналіз часових рядів глобальних продуктів NOAA"

    inputs = [{
        "type": 'dropdown',
        "label": 'Оберіть часовий ряд:',
        "options": [
            {"label": "VCI", "value": "VCI"},
            {"label": "TCI", "value": "TCI"},
            {"label": "VHI", "value": "VHI"}],
        "value": 'VCI',
        "key": 'ticker1',
        "action_id": "update_data"},
        {
            "type": 'dropdown',
            "label": 'Оберіть область:',
            "options": [
                {"label": "Черкаська", "value": "1"},
                {"label": "Чернігівська", "value": "2"},
                {"label": "Чернівецька", "value": "3"},
                {"label": "Респуб. Крим", "value": "4"},
                {"label": "Дніпропетровська", "value": "5"},
                {"label": "Донецька", "value": "6"},
                {"label": "Ів.-Франківська", "value": "7"},
                {"label": "Харківська", "value": "8"},
                {"label": "Херсонська", "value": "9"},
                {"label": "Хмельницька", "value": "10"},
                {"label": "Київська", "value": "11"},
                {"label": "м. Київ", "value": "12"},
                {"label": "Кіровоградська", "value": "13"},
                {"label": "Луганська", "value": "14"},
                {"label": "Львівська", "value": "15"},
                {"label": "Миколаївська", "value": "16"},
                {"label": "Одеська", "value": "17"},
                {"label": "Полтавська", "value": "18"},
                {"label": "Рівненська", "value": "19"},
                {"label": "м. Севастополь", "value": "20"},
                {"label": "Сумська", "value": "21"},
                {"label": "Тернопільська", "value": "22"},
                {"label": "Закарпатська", "value": "23"},
                {"label": "Вінницька", "value": "24"},
                {"label": "Волинська", "value": "25"},
                {"label": "Запорізька", "value": "26"},
                {"label": "Житомирська", "value": "27"}],
            "value": 'VCI',
            "key": 'ticker2',
            "action_id": "update_data"},
        {
            "type": 'dropdown',
            "label": 'Оберіть рік початку спостереження:',
            "options": [
                {"label": "1982", "value": "1982"},
                {"label": "1983", "value": "1983"},
                {"label": "1984", "value": "1984"},
                {"label": "1985", "value": "1985"},
                {"label": "1986", "value": "1986"},
                {"label": "1987", "value": "1987"},
                {"label": "1988", "value": "1988"},
                {"label": "1989", "value": "1989"},
                {"label": "1990", "value": "1990"},
                {"label": "1991", "value": "1991"},
                {"label": "1992", "value": "1992"},
                {"label": "1993", "value": "1993"},
                {"label": "1994", "value": "1994"},
                {"label": "1995", "value": "1995"},
                {"label": "1996", "value": "1996"},
                {"label": "1997", "value": "1997"},
                {"label": "1998", "value": "1998"},
                {"label": "1999", "value": "1999"},
                {"label": "2000", "value": "2000"},
                {"label": "2001", "value": "2001"},
                {"label": "2002", "value": "2002"},
                {"label": "2003", "value": "2003"},
                {"label": "2004", "value": "2004"},
                {"label": "2005", "value": "2005"},
                {"label": "2006", "value": "2006"},
                {"label": "2007", "value": "2007"},
                {"label": "2008", "value": "2008"},
                {"label": "2009", "value": "2009"},
                {"label": "2010", "value": "2010"},
                {"label": "2011", "value": "2011"},
                {"label": "2012", "value": "2012"},
                {"label": "2013", "value": "2013"},
                {"label": "2014", "value": "2014"},
                {"label": "2015", "value": "2015"},
                {"label": "2016", "value": "2016"},
                {"label": "2017", "value": "2017"},
                {"label": "2018", "value": "2018"},
                {"label": "2019", "value": "2019"},
                {"label": "2020", "value": "2020"},
                {"label": "2021", "value": "2021"},
                {"label": "2022", "value": "2022"}],
            "value": 'VCI',
            "key": 'ticker3',
            "action_id": "update_data"},
        {
            "type": 'dropdown',
            "label": 'Оберіть рік кінця спостереження:',
            "options": [
                {"label": "1982", "value": "1982"},
                {"label": "1983", "value": "1983"},
                {"label": "1984", "value": "1984"},
                {"label": "1985", "value": "1985"},
                {"label": "1986", "value": "1986"},
                {"label": "1987", "value": "1987"},
                {"label": "1988", "value": "1988"},
                {"label": "1989", "value": "1989"},
                {"label": "1990", "value": "1990"},
                {"label": "1991", "value": "1991"},
                {"label": "1992", "value": "1992"},
                {"label": "1993", "value": "1993"},
                {"label": "1994", "value": "1994"},
                {"label": "1995", "value": "1995"},
                {"label": "1996", "value": "1996"},
                {"label": "1997", "value": "1997"},
                {"label": "1998", "value": "1998"},
                {"label": "1999", "value": "1999"},
                {"label": "2000", "value": "2000"},
                {"label": "2001", "value": "2001"},
                {"label": "2002", "value": "2002"},
                {"label": "2003", "value": "2003"},
                {"label": "2004", "value": "2004"},
                {"label": "2005", "value": "2005"},
                {"label": "2006", "value": "2006"},
                {"label": "2007", "value": "2007"},
                {"label": "2008", "value": "2008"},
                {"label": "2009", "value": "2009"},
                {"label": "2010", "value": "2010"},
                {"label": "2011", "value": "2011"},
                {"label": "2012", "value": "2012"},
                {"label": "2013", "value": "2013"},
                {"label": "2014", "value": "2014"},
                {"label": "2015", "value": "2015"},
                {"label": "2016", "value": "2016"},
                {"label": "2017", "value": "2017"},
                {"label": "2018", "value": "2018"},
                {"label": "2019", "value": "2019"},
                {"label": "2020", "value": "2020"},
                {"label": "2021", "value": "2021"},
                {"label": "2022", "value": "2022"}],
            "value": 'VCI',
            "key": 'ticker4',
            "action_id": "update_data"}]

    controls = [{
        "type": "button",
        "id": "update_data",
        "label": "Вивести дані"
    }]

    tabs = ["Plot", "Table"]

    outputs = [
        {
            "type": "plot",
            "id": "plot",
            "control_id": "update_data",
            "tab": "Plot"},
        {
            "type": "table",
            "id": "table_id",
            "control_id": "update_data",
            "tab": "Table",
            "on_page_load": True
        }
    ]

    def getData(self, params):
        ticker = params['ticker1', 'ticker2', 'ticker2', 'ticker3', 'ticker4']
        # make call to yahoo finance api to get historical stock data
        api_url='https://www.star.nesdis.noaa.gov/smcd/emb/vci/VH/get_TS_admin.php?country=UKR&provinceID=3&year1=1981&year2=2022&type=Mean'
        #api_url='https: // www.star.nesdis.noaa.gov / smcd / emb / vci / VH / get_TS_admin.php?country = UKR & provinceID = '+ticker[1]+' & year1 = '+ticker[2]+' & year2 = '+ticker[3]+' & type = Mean'
#        api_url = 'https://chartapi.finance.yahoo.com/instrument/1.0/{}/chartdata;type=quote;range=3m/json'.format(
#            ticker)
        result = urllib.request.urlopen(api_url).read()

        data = json.loads(
            result.replace('finance_charts_json_callback( ', '')[:-1])  # strip away the javascript and load json
        self.company_name = data['meta']['Company-Name']
        df = pd.DataFrame.from_records(data['series'])
#        df['Date'] = pd.to_datetime(df['Date'], format='%Y%m%d')
        return df

    def getPlot(self, params):
        df = self.getData(params).set_index('Date').drop(['volume'], axis=1)
        plt_obj = df.plot()
        plt_obj.set_ylabel("Price")
        plt_obj.set_title(self.company_name)
        fig = plt_obj.get_figure()
        return fig












#    def getData(self, params):
#        ticker = params['ticker']
#        if ticker == 'empty':
#            ticker = params['custom_ticker'].upper()

#        xchng = "NASD"
#        param = {
#            'q': ticker,  # Stock symbol (ex: "AAPL")
#            'i': "86400",  # Interval size in seconds ("86400" = 1 day intervals)
#            'x': xchng,  # Stock exchange symbol on which stock is traded (ex: "NASD")
#            'p': "3M"  # Period (Ex: "1Y" = 1 year)
#        }
#        df = get_price_data(param)
#        return df

#    def getPlot(self, params):
#        df = self.getData(params).drop(['Volume'], axis=1)
#        plt_obj = df.plot()
#        plt_obj.set_ylabel("Price")
#        plt_obj.set_xlabel("Date")
#        plt_obj.set_title(params['ticker'])
#        return plt_obj.get_figure()








app = StockExample()
app.launch(port=9093)