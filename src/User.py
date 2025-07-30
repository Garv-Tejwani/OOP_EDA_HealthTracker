import pandas as pd 
import csv
from src.HealthMetric import HealthMetric


class User:
    def __init__(self, name ,age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        self.health_data = []


    def info(self):
        print(f'Name :{self.name}')
        print(f'Age :{self.age}')
        print(f'Gender :{self.gender}')

        
    def add_entry(self , metric):
        self.health_data.append(metric)



    def get_data_as_dataframe(self):
        import pandas as pd
        df=pd.DataFrame([entry.self_dict() for entry in self.health_data])
    
    def save_to_csv(self, filename):
        with open(filename , 'w', newline='') as f:
            writer=csv.DictWriter(f ,fieldnames=['entry_date','steps','calories','sleep_hours','mood'])
            writer.writeheader
            for entry in self.health_data:
                writer.writerow(entry.self_dict())
    

    @classmethod
    def load_from_csv(cls, name , age, gender, filename):
        user=cls(name , age , gender)
        df=pd.read_csv(filename)

        for _,row in df.iterrows:
            metric=HealthMetric( row["date"],
            row["steps"],
            row["calories"],
            row["sleep_hours"],
            row["mood"])
            
            user.add_entry(metric)
        return user 