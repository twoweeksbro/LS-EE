from nycflights13 import flights, planes
import pandas as pd
import matplotlib.pyplot as plt
flights.info()

planes.info()

planes.head()

#
merged_df = pd.merge(planes, flights, on='tailnum', how='left')
#
merged_df.isna().sum()
merged_df2 = pd.merge(planes, flights, on='tailnum', how='right')
merged_df2 = pd.merge(planes, flights, on='tailnum', how='inner')

merged_df.info()
merged_df2.info()


planes.head()
planes.size
planes['type'].value_counts()
# Fixed wing multi engine     3292 가 대부분

planes['manufacturer'].value_counts()
# 보잉 1630개 에어버스 400
planes['model'].value_counts()
planes['seats'].value_counts()

planes['speed'].value_counts()
planes['speed'].isna().sum()
planes['speed'].size
# 총 3322중 3299 가 nan 값.

planes['engines'].value_counts()
# Turbo-fan 2750ro, Turbo-jet 535 등


planes.info()
planes.head()
# 3322 개 가량
flights.info()
flights.head(10)
# 33000개 가량
merged_df.info()
# 280000개 가량
merged_df.columns

# planes(year)제조년도 와 지연시간 상관관계 #
# planes(model) - flights(origin) 상관관계 #

# planes(seats)가 많으면 지연시간이 긴가??  ##
# flights(airtime) - planes(seats)  상관관계 ##

# flights(airtime) - planes(seats) 상관관계: 0.52 상관관계 있다.    ### 
# 특정 제조사(manufacturer)에서 만든 비행기가 고장 때문에 지연이 생기나? ###

# flights(carrier)어느 항공사가 최신 기종  planes(year)을 사용하는지. ####
# 월별 좌석수 상관관계 ####


seats_s = merged_df['seats'].value_counts()
seats_s.sort_index()
merged_df.columns
test = merged_df.groupby(['seats'])['dep_delay'].mean().sort_values(ascending=False)
test = merged_df.groupby(['seats'])['arr_delay'].mean().sort_values(ascending=False)


# 좌석 수와 지연시간 산점도
plt.scatter(merged_df['seats'], 
            merged_df['dep_delay'],
            alpha=0.3)
plt.show()

plt.scatter(merged_df['seats'], 
            merged_df['arr_delay'],
            alpha=0.3)
plt.show()

merged_df.columns
merged_df['air_time']


# 비행 시간과 지연시간 산점도
plt.scatter(merged_df['air_time'], 
            merged_df['arr_delay'], 
            alpha=0.3,
            s=3)
plt.show()

plt.scatter(merged_df['air_time'], 
            merged_df['dep_delay'])
plt.show()



plt.figure(figsize=(6,4))       
plt.hist(merged_df['dep_delay'], 
         bins=50, 
         edgecolor='black', 
         alpha=0.7)  # bin: 상자, bins: 상자 몇개?
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()


#
import seaborn as sns

from statsmodels.graphics.mosaicplot import mosaic
import matplotlib.pyplot as plt

# 히트맵 그리기
corr_mat = flights.select_dtypes('number').corr()
plt.figure(figsize=(10,10))
sns.heatmap(corr_mat, annot=True,
            cmap="coolwarm", fmt=".2f", linewidths=0.5)
plt.title("Heatmap of Feature Correlations")
plt.show()

# 히트맵 그리기
palne_mat = planes.select_dtypes('number').corr()
plt.figure(figsize=(10,10))
sns.heatmap(palne_mat, annot=True,
            cmap="coolwarm", fmt=".2f", linewidths=0.5)
plt.title("Heatmap of Feature Correlations")
plt.show()

# 히트맵 그리기
merged_mat = merged_df.select_dtypes('number').corr()
plt.figure(figsize=(10,10))
sns.heatmap(merged_mat, annot=True,
            cmap="coolwarm", fmt=".2f", linewidths=0.5)
plt.title("Heatmap of Feature Correlations")
plt.show()

planes.info()
flights.info()


plt.plot(flights['Date'], df_timeseries['Value'], marker='o', linestyle='-')
plt.xlabel("Date")
plt.ylabel("Value")
plt.title("Time Series Line Graph")
plt.xticks(rotation=45)
plt.show()


# flights(carrier)어느 항공사가 최신 기종  planes(year)을 사용하는지. ####

merged_df['year_x']

carrier_plaens_year_mean = merged_df.groupby('carrier')['year_x'].mean()

plt.ylim(1960,2018)
plt.bar(carrier_plaens_year_mean.index, carrier_plaens_year_mean)

merged_df['carrier'].value_counts()


# 월별 좌석수 상관관계 ####  
merged_df.groupby('month')['seats'].mean()



# 
models = planes['model'].value_counts()

modelss = merged_df['model'].value_counts()




len(models[models>30])
models.sort_values(ascending=False)

valid_models = models[models>30].index
filtered_data = merged_df[merged_df['model'].isin(valid_models)]


plt.figure(figsize=(15,15), dpi=500)
fig, ax = plt.subplots(figsize=(15, 15), dpi=300)  # 크기 및 해상도 조정
mosaic(filtered_data, ['model', 'origin'], 
       title="mosaic", ax=ax)
plt.show()




# hour - delay


merged_df.groupby(['manufacturer'])['arr_delay'].mean().sort_values()


# 지연시간 히스토그램
flights.columns[flights.columns.str.contains('delay')]


# 히스토그램 그리기



arr_del_desc = flights['arr_delay'].describe()

q1 = arr_del_desc['25%']
q3 = arr_del_desc['75%']
iqr = q3-q1
lower_boundary = q1 - (iqr*1.5)
upper_boundary = q3 + (iqr*1.5)

flights.shape
planes.columns
f_df = flights[(lower_boundary <= flights['arr_delay'] ) & (flights['arr_delay'] <=upper_boundary )]


plt.figure(figsize=(6,4))       
plt.hist(f_df['arr_delay'], 
         bins=20, 
         edgecolor='black', 
         alpha=0.7)  # bin: 상자, bins: 상자 몇개?
plt.xlabel("arr_delay")
plt.ylabel("Frequency")
plt.show()


def PreProcessing(df, column):
    desc = df[column].describe()

    q1 = desc['25%']
    q3 = desc['75%']
    iqr = q3-q1
    lower_boundary = q1 - (iqr*1.5)
    upper_boundary = q3 + (iqr*1.5)

    planes.columns
    f_df = flights[(lower_boundary <= flights['arr_delay'] ) & (flights['arr_delay'] <=upper_boundary )]





flights['arr_delay'].describe()
flights['dep_delay'].describe()


