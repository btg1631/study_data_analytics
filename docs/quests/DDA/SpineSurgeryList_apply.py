import pandas as pd
data =  pd.read_csv("./docs/csv/SpineSurgeryList.csv")
df_SSL = pd.DataFrame(data)

def BMI(x):
    weight = x["체중"]
    height = x["신장"]
    height = height*0.01
    result = weight/(height**2)
    return result

df_SSL["BMI"] = df_SSL[["체중", "신장"]].apply(BMI, axis=1)

print(df_SSL["BMI"])
pass


def hour(x):
    hour = x // 60 # 시간
    return hour
    
def minute(x):
    minute = x % 60 # 분
    return minute
    
df_SSL["hour"] = df_SSL[["수술시간"]].apply(hour, axis=1)
df_SSL["minute"] = df_SSL[["수술시간"]].apply(minute, axis=1)

# Cannot convert non-finite values (NA or inf) to integer
df_SSL["hour"] = df_SSL["hour"].fillna(0).astype(int)
df_SSL["minute"] = df_SSL["minute"].fillna(0).astype(int)

print(df_SSL[["hour", "minute"]])
pass