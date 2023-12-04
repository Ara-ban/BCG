import pandas as pd

aout_2023=pd.read_csv('./temp_data/aout_2023.csv',sep=';')
avril_2023=pd.read_csv('./temp_data/avril_2023.csv',sep=';')
fev_2023=pd.read_csv('./temp_data/fev_2023.csv',sep=';')
jan_2023=pd.read_csv('./temp_data/jan_2023.csv',sep=';')
juillet_2023=pd.read_csv('./temp_data/juillet_2023.csv',sep=';')
juin_2023=pd.read_csv('./temp_data/juin_2023.csv',sep=';')
mai_2023=pd.read_csv('./temp_data/mai_2023.csv',sep=';')
mars_2023=pd.read_csv('./temp_data/mars_2023.csv',sep=';')
nov_2023=pd.read_csv('./temp_data/nov_2023.csv',sep=';')
oct_2023=pd.read_csv('./temp_data/oct_2023.csv',sep=';')
sep_2023=pd.read_csv('./temp_data/sep_2023.csv',sep=';')
Dec_2022=pd.read_csv('./temp_data/Dec_2022.csv',sep=';')
nov_2022=pd.read_csv('./temp_data/nov_2022.csv',sep=';')

def preprocess(temp_df):
    temp_df[['temp_min', 'temp_max']] = temp_df['Jour_Temp'].str.extract(r'(\d+)°C/(\d+)°C')
    temp_df['temp_min'] = pd.to_numeric(temp_df['temp_min'])
    temp_df['temp_max'] = pd.to_numeric(temp_df['temp_max'])
    temp_df['precipitation']=temp_df['Jour_precipitation'].str.extract(r'([\d.]+)').astype(float)
    temp_df.drop('Jour_Temp',axis=1,inplace=True)
    temp_df.drop('Jour_precipitation',axis=1,inplace=True)
jan_2023['precipitation']=jan_2023['Jour_precipitation'].str.extract(r'([\d.]+)').astype(float)
jan_2023.drop('Jour_precipitation',axis=1,inplace=True)

preprocess(nov_2022)
preprocess(Dec_2022)
preprocess(fev_2023)
preprocess(mars_2023)
preprocess(avril_2023)
preprocess(mai_2023)
preprocess(juillet_2023)
preprocess(juin_2023)
preprocess(aout_2023)
preprocess(sep_2023)
preprocess(oct_2023)
preprocess(nov_2023)

datasets=[nov_2022,Dec_2022,jan_2023,fev_2023,mars_2023,avril_2023,mai_2023,juin_2023,juillet_2023,aout_2023,sep_2023,oct_2023,nov_2023]
temperature_df = pd.concat(datasets, axis=0, ignore_index=True)

temperature_df.to_csv('./datasets/temperature_daily_df.csv')