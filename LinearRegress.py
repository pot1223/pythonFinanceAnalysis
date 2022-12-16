!pip install pandas-datareader # 판다스 데이터리더 기반 API로 주식 데이터를 얻을 수 있다 
from pandas_datareader import data as pdr 

!pip install yfinance  # 야후 파이낸스 API로 주식 데이터를 얻을 수 있다 
import yfinance as yf

# 주식 데이터 다운로드 
yf.pdr_override() 
dow = pdr.get_data_yahoo('^DJI', '2000-01-04') # 2000년 이후 다우존스 지수 데이터 다운로드 
kospi = pdr.get_data_yahoo('^KS11', '2000-01-04') # 2000년 이후 코스피 데이터 다운로드 

import matplotlib.pyplot as plt
plt.figure(figsize=(9,5))
plt.plot(dow.index, dow.Close, 'r--', label = "Dow Jones Industrial") # 다우존스 지수를 붉은 점선으로 출력 
plt.plot(kospi.index, kospi.Close , 'b', label = "KOSPI") # 코스피를 푸른 실선으로 출력 
plt.grid(True)
plt.legend(loc = "best")
plt.show

d = (dow.Close / dow.Close.loc["2000-01-04"]) * 100  # 금일 다우존스 지수를 2000년 1월 4일 다우존스 지수로 나눈 뒤 100을 곱함 (지수화)
k = (kospi.Close / kospi.Close.loc["2000-01-04"]) * 100 # 금일 코스피 지수를 2000년 1월 4일 KOSPI 지수로 나눈 뒤 100을 곱함 (지수화)
plt.figure(figsize=(9,5))
plt.plot(d.index, d, 'r--', label = "Dow Jones Industrial Average") # 다우존스 지수를 붉은 점선으로 출력 
plt.plot(k.index, k , 'b', label = "KOSPI") # 코스피를 푸른 실선으로 출력 
plt.grid(True)
plt.legend(loc = "best")
plt.show

import pandas as pd
df = pd.DataFrame({'DOW' : dow['Close'], 'KOSPI' : kospi['Close']})
df = df.fillna(method ='bfill') # fillna()를 bfill 방식으로 사용하면 NaN 데이터 바로 뒤의 값으로 NaN 데이터를 채운다 
df = df.fillna(method = 'ffill') # fillna() 를 ffill 방식으로 사용하면 NaN 데이터 바로 앞의 값으로 NaN 데이터를 채운다 

plt.scatter(df['DOW'], df["KOSPI"], marker='.') # 산점도로 다우존스 지수와 코스피 지수의 관계를 나타냈다. 점의 분포가 직선 형태에 가까울 수록 직접적인 관계가 있다고 본다 
plt.xlabel('Dow Jones Indsutrial Average')
plt.ylabel('KOSPI')

!pip install scipy
from scipy import stats
regr = stats.linregress(df['DOW'], df['KOSPI']) # 일반선형회귀식
regr_line = f"Y = {regr.slope:.2f} * X + {regr.intercept:.2f}"
plt.figure(figsize=(7,7))
plt.plot(df['DOW'],df['KOSPI'], '.')
plt.plot(df['DOW'], regr.slope * df['DOW'] + regr.intercept, 'r')
plt.legend(['DOW X KOSPI', regr_line])
plt.title(f'DOW X KOSPI (R={regr.rvalue:.2f})')
plt.xlabel('Dow Jones Industrial Average')
plt.ylabel('KOSPI')
plt.show()
r_value = df['DOW'].corr(df['KOSPI']) # 상관계수
r_squared = r_value ** 2 # 상관계수를 제곱해서 결정계수를 구한다 
print(r_value, r_squared)
