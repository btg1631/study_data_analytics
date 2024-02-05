# 📈 study_data_analytics
<details> 
  <summary>Titanic_dataset</summary>

- [Titanic_dataset](https://github.com/yojulab/study_data_analytics/blob/main/datasets/TitanicFromDisaster_test.csv)

|*|Variable|Definition|Key|분석가 의견|
|--|--|--|--|--|
|1||PassengerId|승객 unique id||수치형|
|2||Pclass|티켓의 클래스|1, 2, 3|범주형(순서형)|
|3||Name|이름||범주형|
|4|Sex|성별|male, female|범주형|
|5|Age|나이||수치형|
|6|SibSp|함께 탑승한 형제자매, 배우자의 수|0, 1, 2, 3, 4, 5, 8|수치형|
|7|Parch|함께 탑승한 부모자녀의 수|0, 1, 3, 2, 4, 6, 5, 9|수치형|
|8|Ticket|티켓 번호||범주형|
|9|Fare|티켓 요금||수치형|
|10|Cabin|객실 번호|nan, A00, B00, C00, D00, E00 ... |범주형(순서형)|
|11|Embarked|승선한 항구|Q, S, C|범주형|
</details>

<details> 
  <summary>SpineSurgeryList</summary>

- [SpineSurgeryList](https://github.com/yojulab/study_data_analytics/blob/main/datasets/SpineSurgeryList.csv)

|*|Variable|Definition|정상 범위|Key|분석가 의견|
|--|--|--|--|--|--|
|1|환자ID|환자를 식별하는 고유한 ID|없음||범주형, 분석에 맞지 않음|
|2|Large Lymphocyte|혈액 내 큰 림프구 수치를 나타내는 지표|1,500-4,500 / μL||수치형|
|3|Location of herniation	|탈출한 디스크의 위치로 매개변수|없음|1, 2, 3, 4, 5|범주형(순서형), 각 숫자가 특정 디스크의 위치를 나타냄|
|4|ODI|척추 통증 장애 지수로, 일상 생활에서 발생하는 제한 정도를 평가하는 지표|0-100||수치형|
|5|가족력|질병이나 유전적 소인이 부모나 가족 선조에 보이는 경우|없음(또는 해당 질환)|0.,  1., nan|범주형, 결측치(nan) 존재|
|6|간질성폐질환|폐 건강 상태를 나타내는 지표|없음 또는 치료 후 정상|0, 1|범주형|
|7|고혈압여부|고혈압 유무를 나타내는 지표|정상: 90/60-120/80 mmHg|0, 1|범주형|
|8|과거수술횟수|과거 수술을 받은 횟수를 나타내는 지표|0 이상|0, 1, 2, 3|범주형|
|9|당뇨여부|당뇨병 유무를 나타내는 지표|정상: 공복혈당 < 100 mg/dL|0, 1|범주형|
|10|말초동맥질환여부|말초 동맥 질환 유무를 나타내는 지표|없음 또는 치료 후 정상|0, 1|범주형|
|11|빈혈여부|빈혈 유무를 나타내는 지표|여성: 헤모글로빈 < 12 g/dL|0, 1|범주형|
|12|성별|남성 또는 여성 성별을 나타내는 지표|없음|1, 2|범주형|
|13|스테로이드치료|스테로이드 치료 여부를 나타내는 지표|없음 또는 치료 후 정상|0, 1|범주형|
|14|신부전여부|신장 건강 상태를 나타내는 지표|없음 또는 치료 후 정상|0, 1|범주형|
|15|신장|체내 물질의 정상적인 배설을 도와주는 신장 기능을 나타내는 지표|여성: 70-140 mL/min/1.73 m²||수치형(연속형)|
|16|심혈관질환|심혈관 건강 상태를 나타내는 지표|없음 또는 치료 후 정상|0, 1|범주형|
|17|암발병여부|암 발생 여부를 나타내는 지표|없음 또는 발병 후 치료|0, 1|범주형|
|18|연령|나이를 나타내는 지표|0 이상||수치형|
|19|우울증여부|우울증 유무를 나타내는 지표|없음 또는 치료 후 정상|0, 1, 2|범주형, 이상값(2) 존재|
|20|입원기간|입원한 기간을 나타내는 지표|0 이상||수치형|
|21|입원일자|입원일을 나타내는 지표|없음||수치형|
|22|종양진행여부|종양의 진행 상태를 나타내는 지표|없음 또는 치료 후 정상|0, 1|범주형|
|23|직업|환자의 직업을 나타내는 지표|없음 또는 해당 직업|자영업, 운동선수, 특수전문직, 주부, 사업가, nan, 건설업, 운수업, 사무직, 공무원, 농업, 의료직, 학생, 군인, 노동직, 교사, 예술가, 무직|범주형|
|24|체중|체중을 나타내는 지표|정상: 18.5-24.9 kg/m²||수치형(연속형)|
|25|퇴원일자|퇴원일을 나타내는 지표|없음||수치형|
|26|헤모글로빈수치|혈중 헤모글로빈 농도를 나타내는 지표|여성: 12-16 g/dL||수치형|
|27|혈전합병증여부|혈전 합병증 유무를 나타내는 지표|없음 또는 치료 후 정상|0, 1|범주형|
|28|환자통증정도|환자의 통증 정도를 평가하는 지표|0-10(10이 가장 심각)|1, 2, 3, 4, 5, 6, 7, 8, 9, 10|범주형(순서형)|
|29|흡연여부|흡연 여부를 나타내는 지표|없음 또는 해당 여부|0, 1|범주형|
|30|통증기간(월)|통증이 시작된 지난 기간을 나타내는 지표|0 이상||수치형|
|31|수술기법|수술 시 사용된 기술을 나타내는 지표|없음 또는 해당 기술|TELD, IELD, nan|범주형, 결측치(nan) 존재|
|32|수술시간|수술 소요 시간을 나타내는 지표|0 이상||수치형|
|33|수술실패여부|수술 실패 여부를 나타내는 지표|없음 또는 해당 여부|0, 1|범주형|
|34|수술일자|수술을 받은 날짜를 나타내는 지표|없음||수치형|
|35|재발여부|척추 통증이 재발되었는지 여부를 나타내는 지표|없음 또는 해당 여부|0, 1|범주형|
|36|혈액형|환자의 혈액형을 나타내는 지표|없음 또는 해당 혈액형|RH+A, RH+B, RH+O, RH+AB|범주형|
|37|전방디스크높이(mm)|전방 디스크의 높이를 나타내는 지표|0 이상||수치형|
|38|후방디스크높이(mm)|후방 디스크의 높이를 나타내는 지표|0 이상||수치형|
|39|지방축적도|지방 축적 정도를 나타내는 지표|정상: 20-25%||수치형|
|40|Instability|척추 안정성을 나타내는 지표|없음 또는 해당 여부|0, 1|범주형|
|41|MF + ES|혼합 신경병증 및 대량 열 치료(미세파 관리 및 전기 자극)로 수행된 치료법|없음 또는 해당 여부||수치형|
|42|Modic change|검은색과 밝은색의 조합으로 척추의 변형을 표시하는 방법으로, 척추 통증과 관련이 있을 수 있다.|없음 또는 해당 여부|0, 1, 2, 3|범주형
|43|PI|척추 곡률을 나타내는 지표|30-40도||수치형|
|44|PT|척추 곡률을 나타내는 지표|13-17도||수치형|
|45|Seg Angle(raw)|척추 각도를 나타내는 지표|없음||수치형|
|46|Vaccum disc|Vaccum disk는 디스크의 최종 단계로, 이 상태에서 쉽게 부러져 다른 퇴행성 디스크 질환을 유발한다.|없음 또는 해당 여부|0, 1|범주형|
|47|골밀도|골의 밀도를 나타내는 지표|약 1 g/cm³ 이상||수치형|
|48|디스크단면적|디스크 단면적을 나타내는 지표|50-200 px²||수치형|
|49|디스크위치|디스크의 위치를 나타내는 지표|없음 또는 해당 위치|4, 5, 3, 2, 45, 25, 12, 34, 23, 11, 10, 35, 1|범주형(순서형), 각 숫자가 특정 디스크 위치를 나타냄|
|50|척추이동척도|척추 이동 범위를 나타내는 지표|10-15 °|Down, Up, Middle, Extremely down, Extremely up|범주형|
|51|척추전방위증|척추의 사진에서 전방위증을 발견한 경우의 수준을 나타내는 지표|없음 또는 해당 위치|0, 1|범주형|
</details>


## 💻 Pandas
|*|제목|code|설명|비고|
|--|--|--|--|--|
|1|series|[pandas_series](./docs/pandas/00_pandas_series.ipynb)|Series = index + value||
|2|DataFrame|[pandas_DataFrame](./docs/pandas/02_pandas_DataFrame.ipynb)|DataFrame = (Series + Series + ..) + column||
|3|datetimes|[pandas_datetimes](./docs/pandas/03_pandas_datetimes.ipynb)|날짜형 데이터 다루기||
|4|apply|[pandas_apply](./docs/DDAs/04_pandas_apply.py)|판다스에서 함수 다루기||
|5|aggregation|[pandas_aggregation](./docs/pandas/05_pandas_aggregations.ipynb)|집계 함수 다루기|aggfunc|
|6|filtering|[pandas_filtering](./docs/pandas/06_pandas_filteringconditional.ipynb)|조건 필터링|boolean indexing/query|
|7|missingvalues|[pandas_missingvalues](./docs/pandas/07_pandas_preprocessing_missingvalues.ipynb)|결측치 전처리||
|8|outlier|[pandas_outlier](./docs/pandas/08_pandas_preprocessing_outlier.ipynb)|이상치 전처리||
|9|useful|[pandas_useful](./docs/pandas/09_pandas_usefuls.ipynb)|연속형 -> 범주형 전환||
|10|merge|[pandas_merge](./docs/pandas/10_pandas_merges.ipynb)|여러 데이터 합치기|concat()|

## 💻 visuallization
|*|제목|code|설명|비고|
|--|--|--|--|--|
|0|example|[example](./docs/visuallization/visuallization_example.ipynb)|주차별 환자 입원/퇴원 추이 시각화와 분석||
|1|matplotlib korean|[visuallization_korean](./docs/visuallization/01_matplotlib_simple_korean.ipynb)|matplotlib 한글 폰트 적용||
|2|univariate|[visuallization_univariate](./docs/visuallization/02_univariate.ipynb)|단일변수 시각화||
|3|multivariate|[visuallization_multivariate](./docs/visuallization/03_visuallization_multivariate.ipynb)|다변수 시각화||



# 📈 quests
## 💻 DDA(Descriptive Data Analysis) 묘사 데이터 분석
- 통계 관점으로 특성 확인(현재 모습 요약) : 평균, 표준편차, 빈도수, 백분위수 등

|*|code|설명|비고|
|--|--|--|--|
|1|[extract_5Rank](./docs/quests/DDA/extract_5Rank.ipynb)|범주형 타입 일부 추출 후 상위/하위 3위를 시각화(barplot)||
|2|[SpineSurgeryList_datetime](./docs/quests/DDA/SpineSurgeryList_datetime.ipynb)|가장 오랜 입원 일자 중 5위까지 시각화(barplot), 수술 일자를 분해(월, 주, 일)하고 시각화(countplot)||
|3|[SpineSurgeryList_apply](./docs/quests/DDA/SpineSurgeryList_apply.py)|apply() 적용 BMI 컬럼 생성|option: 수술시간(총 분) -> 시분 표시한 컬럼 생성|


## 💻 EDA(Exploratory Data Analysis) 탐색 데이터 분석
- 데이터 증상 탐색을 통한 가설 도출

|*|code|설명|비고|
|--|--|--|--|
|1|[multivariate_OrdersDeliveryList](./docs/quests)|문제 풀기|[문제](https://docs.google.com/document/d/1NawUP-V9yy1NxywayYHLVC1P4Rtg7YavpT82pnE6938/edit)|
|2|[preprocessing_titanic_train](./docs/quests/EDAs/preprocessing_titanic_train.ipynb)|문제 풀기|[문제](https://docs.google.com/document/d/19zaaxXw1-Px4e1bKmit6h233myLWJKaeqFf-rfsKJw0/edit)|
|3|[EDA_LetalCarOfContractType](./docs/quests/EDAs/EDA_LetalCarOfContractType.ipynb)|제안 3: 연체 위험도 예측|[csv](./docs/csv/LetalCarOfContractType.csv)|
|4|[EDA_ShoppingMallDeliveryWithDate](./docs/quests/EDAs/EDA_ShoppingMallDeliveryWithDate.ipynb)|제안 8: 주문량 변동성 분석 및 예측|[csv](./docs/csv/ShoppingMallDeliveryWithDate.csv)|
|5|[EDA_kaggle_air_quality_in_covid19](./docs/quests/EDAs/)|제안1 : 공기 질 지표의 시간별 변화 분석|[csv](https://www.kaggle.com/datasets/aestheteaman01/air-quality-across-countries-in-covid19)|

