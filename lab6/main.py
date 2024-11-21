import pandas as pd
import numpy as np

try:
    # exercise 1
    bronze = pd.read_csv("Medals/Bronze.csv")
    silver = pd.read_csv("Medals/Silver.csv")
    gold = pd.read_csv("Medals/Gold.csv")
    # print(gold.head())
except FileNotFoundError as e:
    print(e)
except pd.errors.EmptyDataError as e:
    print(e)
except Exception as e:
    print(e)

try:
    # exercise 2
    weather = pd.read_csv("Week_6/weather2.csv")
    temps_f = weather[['Min TemperatureF', 'Mean TemperatureF', 'Max TemperatureF']]
    temps_c = (temps_f - 32) * 5/9
    temps_c.columns = temps_c.columns.str.replace('F', 'C')
    # print(temps_c.head())
except FileNotFoundError as e:
    print(e)
except KeyError as e:
    print(e)
except Exception as e:
    print(e)

try:
    # exercise 3
    combined = pd.concat([bronze, silver])
    # print(combined.head())
except ValueError as e:
    print(e)
except Exception as e:
    print(e)

try:
    jan = pd.read_csv('Sales/sales-jan-2015.csv', parse_dates=True, index_col='Date')
    feb = pd.read_csv('Sales/sales-feb-2015.csv', parse_dates=True, index_col='Date')
    mar = pd.read_csv('Sales/sales-mar-2015.csv', parse_dates=True, index_col='Date')

    print(jan.columns)

    jan_units = jan['Units']
    feb_units = feb['Units']
    mar_units = mar['Units']
    
    jan['Units'] = pd.to_numeric(jan['Units'])
    feb['Units'] = pd.to_numeric(feb['Units'])
    mar['Units'] = pd.to_numeric(mar['Units'])

    
    df_quarter = pd.concat([jan['Units'], feb['Units'], mar['Units']], axis=1, keys=['jan', 'feb', 'mar'], join='outer')
    df_quarter_mean = df_quarter.mean()
    print("mean", df_quarter_mean)

    greater_than_mean = df_quarter[(df_quarter['jan'] > df_quarter_mean['jan']) | 
                                  (df_quarter['feb'] > df_quarter_mean['feb']) | 
                                  (df_quarter['mar'] > df_quarter_mean['mar'])] 
    
    print(greater_than_mean)   
    # quarter1 = quarter1.sort_index()
  
    # print(quarter1.loc['2015-01-27':'2015-02-02'])
    # print(quarter1.loc['2015-02-26':'2015-03-07'])
    # mean = quarter1['Units'].mean()
    # print(quarter1.head())
    # print("mean:", mean)
    # print("greater than mean", greater_than_mean.head())
    
    # total_units_sold = quarter1.sum()
    # print(total_units_sold)
except FileNotFoundError as e:
    print(e)
except KeyError as e:
    print(e)
except Exception as e:
    print(e)

try:
    medal_list = [bronze, silver, gold]
    medals = pd.concat(medal_list, axis=1, keys=['bronze', 'silver', 'gold'], join='inner')
    # print(medals)
except ValueError as e:
    print(e)
except Exception as e:
    print(e)
