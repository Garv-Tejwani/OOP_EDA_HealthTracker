from src.User import User 
from src.HealthMetric import HealthMetric
import csv
import pandas as pd
import matplotlib.pyplot as plt


user = User('garv',18,'male')



user_data_1= pd.read_csv('data/Health_Data.csv')
user_data_1['entry_date']=pd.to_datetime(user_data_1['entry_date'])

plt.plot(user_data_1['entry_date'],user_data_1['steps'],marker='o')
plt.title('steps over time')
plt.xlabel('entry_date')
plt.ylabel('steps')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

