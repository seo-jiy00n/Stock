import FinanceDataReader as fdr
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

samsung = fdr.DataReader("005930", "2020", "2023-6-1")
kakao = fdr.DataReader("035720", "2020", "2023-6-1")
sk = fdr.DataReader("000660", "2020", "2023-6-1")
naver = fdr.DataReader("035420", "2020", "2023-6-1")
hyundai = fdr.DataReader("005380", "2020", "2023-6-1")

# print(samsung.head())
# print(kakao.head())
# print(sk.head())
# print(naver.head())
# print(hyundai.head())
#
# # 삼성전자 단일 종목 수익률
# samsungDayReturn = (samsung['Close'] / samsung['Close'].shift(1)).fillna(1)
# print(samsungDayReturn)
#
# # 삼성전자 누적수익률
# samsungCumulativeReturn = samsungDayReturn.cumprod()
#
# # cagr
# samsungCagr = samsungCumulativeReturn.iloc[-1] ** (252/len(samsung))
# # mdd
# samsungDd = (samsungCumulativeReturn.cummax() - samsungCumulativeReturn) / samsungCumulativeReturn.cummax() * 100
# samsungMdd = samsungDd.max()
#
# print("cagr: ",samsungCagr)
# print("mdd: ",samsungMdd)

# # 시각화
# plt.figure(figsize=(20, 10))

# # 수익곡선
# plt.subplot(2, 1, 1)
# samsungCumulativeReturn.plot(color="black")
# plt.ylabel("profit", fontsize=20)
#
# # 낙폭곡선
# plt.subplot(2, 1, 2)
# plt.plot(-samsungDd, color="red")
# plt.ylabel("draw down", fontsize=20)
# plt.show()

# 분산투자와 개별 투자 비교
stocks = [samsung, kakao, sk, naver, hyundai]

data = pd.DataFrame()

for stock in stocks:
    data = pd.concat([data, stock['Close']], axis=1)

data.columns = ["samsung", "kakao", "sk", "naver", "hyundai"]

# 개별 일별 자산 수익률
dayReturn = (data / data.shift(1)).fillna(1)
# 개별 자산 누적 수익률
cumReturn = data / data.iloc[0]
# 포트폴리오 비율 : 동일 가중
portWeight = [1/len(data.columns)] * len(data.columns)
# 누적 수익률
portCumReturn = (portWeight * cumReturn).sum(axis=1)

# 결과 비교
plt.figure(figsize=(20, 8))

for stock in cumReturn.columns:
    # 그래프
    cumReturn[stock].plot(label=stock)
    # cagr
    cagr = cumReturn[stock].iloc[-1] ** (252 / len(cumReturn[stock]))
    # mdd
    dd = (cumReturn[stock].cummax() - cumReturn[stock]) / cumReturn[stock].cummax() * 100
    mdd = dd.max()

    print(stock)
    print(f"cagr: {cagr}\nmdd: {mdd}")
    print("=======")

# cagr
cagr = portCumReturn.iloc[-1] ** (252 / len(portCumReturn))
# mdd
dd = (portCumReturn.cummax() - portCumReturn) / portCumReturn.cummax() * 100
mdd = dd.max()

print("portfolio")
print(f"cagr: {cagr}\nmdd: {mdd}")
print("=======")

portCumReturn.plot(label="porfolio", linestyle="dotted", linewidth=3)
plt.legend()
plt.show()