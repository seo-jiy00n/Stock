from django.shortcuts import render

# Create your views here.
import matplotlib.pyplot as plt
# from django.shortcuts import render
import pandas as pd
import FinanceDataReader as fdr
from io import BytesIO
import base64


def main(request):
    return render(request, template_name="stock/graph.html")

def samsung(request):
    samsung = fdr.DataReader('005930', '2020-01-01', '2023-06-01')
    samsungCumulativeReturn = samsung['Close'] / samsung['Close'].iloc[0]   #삼성전자 누적 수익률
    samsungDd = (samsungCumulativeReturn.cummax() - samsungCumulativeReturn) / samsungCumulativeReturn.cummax()   #삼성전자 하락폭

    # 그래프 생성
    fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(20, 10))

    # 수익곡선 그래프
    axes[0].plot(samsungCumulativeReturn, color="black")
    axes[0].set_ylabel("profit", fontsize=20)

    # 낙폭곡선 그래프
    axes[1].plot(-samsungDd, color="red")
    axes[1].set_ylabel("draw down", fontsize=20)

    # 그래프를 이미지로 변환
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()

    # 이미지를 base64로 인코딩
    graphic_s = base64.b64encode(image_png).decode('utf-8')

    return render(request, 'stock/samsung.html', {'graphic_s': graphic_s})

def kakao(request):
    # 카카오 데이터 불러오기
    kakao = fdr.DataReader('035720', '2020-01-01', '2023-06-01')
    kakaoCumulativeReturn = kakao['Close'] / kakao['Close'].iloc[0]  # 카카오 누적 수익률
    kakaoDd = (kakaoCumulativeReturn.cummax() - kakaoCumulativeReturn) / kakaoCumulativeReturn.cummax()  # 카카오 하락폭
    # 그래프 생성
    fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(20, 10))

    # 수익곡선 그래프
    axes[0].plot(kakaoCumulativeReturn, color="black")
    axes[0].set_ylabel("profit", fontsize=20)

    # 낙폭곡선 그래프
    axes[1].plot(-kakaoDd, color="red")
    axes[1].set_ylabel("draw down", fontsize=20)

    # 그래프를 이미지로 변환
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()

    # 이미지를 base64로 인코딩
    graphic_k = base64.b64encode(image_png).decode('utf-8')

    return render(request, 'stock/kakao.html', {'graphic_k': graphic_k})

def hyundai(request):
    # 현대 데이터 불러오기
    hyundai = fdr.DataReader('005380', '2020-01-01', '2023-06-01')
    hyundaiCumulativeReturn = hyundai['Close'] / hyundai['Close'].iloc[0]  # 현대 누적 수익률
    hyundaiDd = (hyundaiCumulativeReturn.cummax() - hyundaiCumulativeReturn) / hyundaiCumulativeReturn.cummax()  # 현대 하락폭
    # 그래프 생성
    fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(20, 10))

    # 수익곡선 그래프
    axes[0].plot(hyundaiCumulativeReturn, color="black")
    axes[0].set_ylabel("profit", fontsize=20)

    # 낙폭곡선 그래프
    axes[1].plot(-hyundaiDd, color="red")
    axes[1].set_ylabel("draw down", fontsize=20)

    # 그래프를 이미지로 변환
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()

    # 이미지를 base64로 인코딩
    graphic_h = base64.b64encode(image_png).decode('utf-8')

    return render(request, 'stock/hyundai.html', {'graphic_h': graphic_h})

def naver(request):
    # 현대 데이터 불러오기
    naver = fdr.DataReader('035420', '2020-01-01', '2023-06-01')
    naverCumulativeReturn = naver['Close'] / naver['Close'].iloc[0]  # 네이버 누적 수익률
    naverDd = (naverCumulativeReturn.cummax() - naverCumulativeReturn) / naverCumulativeReturn.cummax()  # 네이버 하락폭
    # 그래프 생성
    fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(20, 10))

    # 수익곡선 그래프
    axes[0].plot(naverCumulativeReturn, color="black")
    axes[0].set_ylabel("profit", fontsize=20)

    # 낙폭곡선 그래프
    axes[1].plot(-naverDd, color="red")
    axes[1].set_ylabel("draw down", fontsize=20)

    # 그래프를 이미지로 변환
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()

    # 이미지를 base64로 인코딩
    graphic_n = base64.b64encode(image_png).decode('utf-8')

    return render(request, 'stock/naver.html', {'graphic_n': graphic_n})

def sk(request):
    # 현대 데이터 불러오기
    sk = fdr.DataReader('000660', '2020-01-01', '2023-06-01')
    skCumulativeReturn = sk['Close'] / sk['Close'].iloc[0]  # sk 누적 수익률
    skDd = (skCumulativeReturn.cummax() - skCumulativeReturn) / skCumulativeReturn.cummax()  # sk 하락폭
    # 그래프 생성
    fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(20, 10))

    # 수익곡선 그래프
    axes[0].plot(skCumulativeReturn, color="black")
    axes[0].set_ylabel("profit", fontsize=20)

    # 낙폭곡선 그래프
    axes[1].plot(-skDd, color="red")
    axes[1].set_ylabel("draw down", fontsize=20)

    # 그래프를 이미지로 변환
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()

    # 이미지를 base64로 인코딩
    graphic_s = base64.b64encode(image_png).decode('utf-8')

    return render(request, 'stock/sk.html', {'graphic_s': graphic_s})

# 5개 종목
def total(request):
    # 주식 데이터 가져오기
    # stocks = ['005930', '035720', '034730', '035420', '005380']
    stocks = ['005930', '035720', '034730', '035420', '005380']
    data = pd.DataFrame()

    for stock in stocks:
        df = fdr.DataReader(stock, '2020-01-01', '2023-06-01')
        data = pd.concat([data, df['Close']], axis=1)

    data.columns = ['samsung', 'kakao', 'sk', 'naver', 'hyundai']

    # 개별 일별 자산 수익률
    dayReturn = (data / data.shift(1)).fillna(1)
    # 개별 자산 누적 수익률
    cumReturn = data / data.iloc[0]
    # 포트폴리오 비율: 동일 가중
    portWeight = [1 / len(data.columns)] * len(data.columns)
    # 누적 수익률
    portCumReturn = (portWeight * cumReturn).sum(axis=1)

    # 그래프 생성
    plt.figure(figsize=(20, 8))

    for stock in cumReturn.columns:
        # 그래프
        cumReturn[stock].plot(label=stock)
        # CAGR
        cagr = cumReturn[stock].iloc[-1] ** (252 / len(cumReturn[stock]))
        # MDD
        dd = (cumReturn[stock].cummax() - cumReturn[stock]) / cumReturn[stock].cummax() * 100
        mdd = dd.max()

        # print(stock)
        # print(f"CAGR: {cagr}\nMDD: {mdd}")
        # print("=======")

    # CAGR
    cagr = portCumReturn.iloc[-1] ** (252 / len(portCumReturn))
    # MDD
    dd = (portCumReturn.cummax() - portCumReturn) / portCumReturn.cummax() * 100
    mdd = dd.max()

    # print("portfolio")
    # print(f"CAGR: {cagr}\nMDD: {mdd}")
    # print("=======")

    portCumReturn.plot(label="portfolio", linestyle="dotted", linewidth=3)
    plt.legend()

    # 그래프를 이미지로 변환
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()

    # 이미지를 base64로 인코딩
    total = base64.b64encode(image_png).decode('utf-8')

    return render(request, 'stock/total.html', {'total': total})
