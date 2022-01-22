from .models import City_wheather
from sklearn.linear_model import LinearRegression
import numpy as np
cities = City_wheather.objects.all()

forcastday_list = []
today_list = []
day_1_list = np.array([])
day_2_list = np.array([])
day_3_list = []
day_4_list = []
day_5_list = []
day_6_list = []
day_7_list = []

for object in cities:
    forcastday_list.append(object.forcastday)
    today_list.append(object.today)
    day_1_list=np.append(day_1_list,object.day_1)
    day_2_list=np.append(day_2_list,object.day_2)
    day_3_list.append(object.day_3)
    day_4_list.append(object.day_4)
    day_5_list.append(object.day_5)
    day_6_list.append(object.day_6)
    day_7_list.append(object.day_7)

print(day_1_list)
def forcast(forcast_sys, today_info, seven_day_info):
    d1 = day_1_list.reshape(-1, 1)
    d2 = day_2_list.reshape(-1, 1)
    d3 = np.array(day_3_list).reshape(-1, 1)
    d4 = np.array(day_4_list).reshape(-1, 1)
    d5 = np.array(day_5_list).reshape(-1, 1)
    d6 = np.array(day_6_list).reshape(-1, 1)
    d7 = np.array(day_7_list).reshape(-1, 1)
    x = np.concatenate([d1,d2],axis=1)
    print(x)
    y = np.array(today_list)
    reg = LinearRegression().fit(x, y)
    dim_1= np.array(seven_day_info[0]).reshape(-1,1)
    dim_2 =np.array(seven_day_info[1]).reshape(-1,1)
    pred_today = reg.predict(np.concatenate([dim_1,dim_2],axis=1))
    diff_today = today_info - pred_today
    pred_tomorrow = []
    diff_tomorrow = []
    forcast_dict = {
        "for_today": {
            "prediction": pred_today,
            "differ": diff_today
        },
        "for_tomorrow": {
            "prediction": pred_tomorrow,
            "differ": diff_tomorrow
        }

    }
    return forcast_dict
