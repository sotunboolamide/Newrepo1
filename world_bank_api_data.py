import pandas as pd
import wbdata
import pandas as pd
import matplotlib.pyplot as plt

msdat_ind = pd.read_csv('World Bank Indicator IDS.csv')

list_name = [i for i in msdat_ind['Generalized indicator name']]
list_ind = [i for i in msdat_ind['IDS']]

dict_ind = dict(zip(list_ind,list_name))
 
#set up the countries I want
countries = ['NG']
 
#set up the indicator I want (just build up the dict if you want more than one)

 
#grab indicators above for countires above and load into data frame
df = wbdata.get_dataframe(dict_ind, country=countries, convert_date=True)

indicators_list = list(df.columns)
period_list = list(df.index)

for ind in indicators_list:
  
  values = [i for i in df[ind]]

  fin_df = pd.DataFrame({'Indicator':ind, 'Period':period_list , 'State' :'National', 'LGA': 'All', 'Source': 'World Bank', 'Value' : values})

  fin_df.to_csv(f'CSV for {ind}.csv',index = False)