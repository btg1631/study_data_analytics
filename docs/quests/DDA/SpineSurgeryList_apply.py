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

def time(x):
    try:
        hour = int(x // 60) # 시간
        minute = int(x % 60) # 분

        time = f"{hour}:{minute}"
        return pd.to_datetime(f"{time}", format="%H:%M")

    except:
        pass

df_SSL["수술시간_time"] = df_SSL[["수술시간"]].apply(time, axis=1)
df_SSL["수술시간_time"] = df_SSL["수술시간_time"].dt.time

print(df_SSL["수술시간_time"])
pass