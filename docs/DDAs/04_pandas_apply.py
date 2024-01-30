# 데이터 리스트를 생성합니다.
data = {
    "시작일": [
        "2019-01-07 08:56", "2019-02-05 09:30", "2019-03-10 11:00",
        "2019-04-12 10:15", "2019-05-19 12:42", "2019-06-21 13:53",
        "2019-07-28 14:08", "2019-08-15 15:22", "2019-09-18 16:33",
        "2019-10-23 17:44"
    ],
    "완료일_한글": [
        "2019-01-11 오후 05:32", "2019-02-09 오후 04:20", "2019-03-14 오후 06:45",
        "2019-04-16 오후 08:55", "2019-05-23 오후 07:30", "2019-06-25 오후 03:44",
        "2019-08-01 오후 04:16", "2019-08-19 오후 05:47", "2019-09-22 오후 06:00",
        "2019-10-27 오후 09:30"
    ],
    "신청일_수치": [
        20181227, 20190201, 20190306, 20190408, 20190515,
        20190617, 20190724, 20190811, 20190914, 20191019
    ],
    "신청일": [
        "2018.12.27", "2019.02.01", "2019.03.06", "2019.04.08", "2019.05.15",
        "2019.06.17", "2019.07.24", "2019.08.11", "2019.09.14", "2019.10.19"
    ]
}

import pandas as pd
df_datetimes = pd.DataFrame(data)
pass

# '완료일_한글' 컬럼을 datetime 형식으로 변환합니다.
# '오후'는 PM을 의미하므로, 이를 12시간으로 변환해주어야 합니다.
# x => "2019-01-11 오후 05:32" -> "2019-01-11 17:32"
def convert_time(x):
    date, ampm, time = x.split()
    if ampm == "오후" and time != "12:00":
        hour, minute = map(int, time.split(":"))
        time = f"{hour+12 if hour != 12 else hour}:{minute}"
    return pd.to_datetime(f"{date} {time}", format="%Y-%m-%d %H:%M")


pass
df_datetimes['완료일_한글_datetime'] = df_datetimes['완료일_한글'].apply(convert_time)

def recive_params(params):
    return params

df_datetimes[['완료일_한글', '신청일']].apply(recive_params, axis=1)
pass