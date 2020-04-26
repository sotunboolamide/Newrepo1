
import pandas as pd
import wbdata
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime as dt
from email_not import email_change, email_no_change
msdat_ind = pd.read_csv('World Bank Indicator IDS.csv')
com_df = pd.read_csv('Original Dataframe.csv')
#com_df.drop(columns=['date'])
list_name = [i for i in msdat_ind['Generalized indicator name']]
list_ind = [i for i in msdat_ind['IDS']]

dict_ind = dict(zip(list_ind,list_name))
 
#set up the countries I want
countries = ['NG']
 
#set up the indicator I want (just build up the dict if you want more than one)

#grab indicators above for countires above and load into data frame
df = wbdata.get_dataframe(dict_ind, country=countries, convert_date=True)


columns_names =list(df.columns)
name_list =[]
final_rep = pd.DataFrame(columns=columns_names)

for i in range(len(columns_names)):


  name1 =f'{columns_names[i]}'
  name_list.append(name1)
  name1 = pd.to_numeric(df[columns_names[i]]).apply(lambda x: x not in pd.to_numeric(com_df[columns_names[i]]))
  check =[True]
  name_check = 'check' + columns_names[i]
  
  name_check = name1[name1.apply(lambda x : x not in check )]
  final_rep[columns_names[i]] =name_check


if final_rep.empty:
  print('No changes')
  email_no_change()
else :
  print('there are cahnges')
  final_rep.to_csv('NewUpdate.csv')
  email_change()
