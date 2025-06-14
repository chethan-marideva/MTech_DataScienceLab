import pandas as pd
import os
import kagglehub
import matplotlib.pyplot as plot



# Download the dataset using kagglehub
path = kagglehub.dataset_download("jkrithika/chennai-2009-2024-weather-data")
ds_path = os.path.join(path, 'Clean15YearChennaiWeather.csv')

weather_data = pd.read_csv(ds_path)


#print(weather_data.head())


#Task - 1.Drop Date and Date ID from the Dataset
weather_data = weather_data.drop(['date', 'date_id'], axis=1) 
print(weather_data.head(5))

#Task - 2.Compute the number of days with Fog, Partly cloudy, Broken clouds, Drizzle and plot the bar graph.

weather_conditions = ['Fog', 'Partly cloudy', 'Broken clouds', 'Drizzle']

weather_condition_count = {
    condition: weather_data['desc'].str.contains(condition, case=False).sum()
    for condition in weather_conditions
}

plot.bar(weather_condition_count.keys(), weather_condition_count.values(), color='black')
plot.xlabel('Weather Conditions')
plot.ylabel('Number of Days')
plot.title('Number of days with Fog, Partly cloudy, Broken clouds, Drizzle in Chennai')
plot.show()

# 3.Compute the average temperature in each year and plot the results as average temperature vs year.

avg_temp_per_year= weather_data.groupby('year')['temp'].mean()
#print(type(avg_temp_per_year))
plot.plot(avg_temp_per_year.index.tolist(),avg_temp_per_year.values.tolist(), marker='.')
plot.xlabel('Year')
plot.ylabel('Average Temparature')
plot.title('Average temperature in each year in Chennai')
plot.show()

print(avg_temp_per_year)



# 4.Plot histogram for humidity

plot.figure(figsize=(6,6))
plot.hist(weather_data['hum'], bins=20, color='yellow', edgecolor='black')
plot.title('Histogram of Humidity')
plot.xlabel('Humidity')
plot.ylabel('Frequency')
plot.grid(axis='y', alpha=0.75)
plot.show()

# 5.Plot freq polygon of humidity and temp like above for each year.


plot.figure(figsize=(10, 6))

for year, group in weather_data.groupby('year'):

    hum_count, hum_bins, _ = plot.hist(
        group['hum'], 
        bins=20, 
        range=(0,100), 
        density=False, 
        alpha=0, 
        label=None
    )
    hum_center = (hum_bins[1:] + hum_bins[:-1])*0.5
    plot.plot(hum_center, hum_count, label=f'{year} - Humidity')


    temp_count, temp_bins, _ = plot.hist(
        group['temp'], 
        bins=20, 
        range=(-30,50), 
        density=False, 
        alpha=0, 
        label=None
    )
    temp_center = (temp_bins[1:] + temp_bins[:-1])*0.5
    plot.plot(temp_center, temp_count, label=f'{year} - Temp')


plot.title('Frequency Polygon of Humidity and Temp by Year')
plot.xlabel('Values')
plot.ylabel('Frequency')
plot.legend()
plot.grid(axis='y', alpha=0.75)
plot.show()




# 6.Compute Mode value desc.

mode_desc = weather_data['desc'].mode()

print('\nmode for desc column:',mode_desc)


# 7.Convert day name as 0: sunday 1: Monday and so on.
day_to_number_mapper = {
    0:'Monday',
    1:'Tuesday',
    2:'Wednesday',
    3:'Thursday',
    4:'Friday',
    5:'Saturday',
    6:'Sunday',
}
weather_data['day_name'] = weather_data['day_name'].map(day_to_number_mapper)
print('\nConvert day name as 0: sunday 1: Monday and so on.')
print(weather_data)

# 8.Plot average temperature on Sundays,

sunday_weather_data = weather_data[weather_data['day_name'] == 'Sunday']
#print(sunday_weather_data)



sunday_avg_temp = sunday_weather_data.groupby('day_date')['temp'].mean().reset_index()
#print(type(sunday_avg_temp))
plot.figure(figsize=(10, 5))
plot.plot(sunday_avg_temp['day_date'], sunday_avg_temp['temp'], marker='.')
plot.title('Average temperature on Sundays')
plot.xlabel('Day')
plot.ylabel('Temperature')
plot.grid(True)
plot.show()



# 9.Plot a pie chart for barometer value <1001 on sundays.


filtered_sundays = weather_data[
    (weather_data['day_name'] == 'Sunday') & (weather_data['baro'] < 1001)
]


filtered_sundays['baro'].value_counts().plot.pie(
    autopct='%1.1f%%',
    startangle=90,
    shadow=False,
    title='Distribution of Barometric Pressure <1001 on Sundays'
)

plot.axis('equal') 
plot.show()



# 10.Plot which date and month has more reading in each year.

reading_counts = weather_data.groupby(['year', 'month', 'day_date']).size().reset_index(name='reading_count')
print(reading_counts)


max_readings_per_year = reading_counts.loc[reading_counts.groupby('year')['reading_count'].idxmax()]

print(max_readings_per_year)


max_readings_per_year['label'] = max_readings_per_year['day_date'].astype(str) + '-' + max_readings_per_year['month'].astype(str)
print(max_readings_per_year['label'])



labels = max_readings_per_year['year'].astype(str)
values = max_readings_per_year['reading_count']


bars = plot.bar(labels, values, color='grey')


for bar, row in zip(bars, max_readings_per_year.iterrows()):
    plot.text(bar.get_x() + bar.get_width()/2, 
              bar.get_height() + 0.5, 
              f"{row[1]['day_date']}-{row[1]['month']}",
              ha='center', 
              fontsize=9, 
              rotation=45, 
              color='black',
              bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.7))


plot.xlabel('Year')
plot.ylabel('Number of Readings')
plot.title('Date and Month with Most Readings per Year')
plot.tight_layout()
plot.show()