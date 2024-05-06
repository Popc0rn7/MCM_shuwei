import pandas_instruction as pd
import statsmodels.api as sm
# 读取数据并创建时间序列
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller

# 假设你的时间序列是endog

data = pd.read_csv('hainan_output.csv', parse_dates=['year'], index_col='year')
def ARIMA(data,year,p,d,q):
    # 拟合ARIMA模型
    model = sm.tsa.ARIMA(data, order=(p, d, q))  # 这里的(1, 1, 1)是ARIMA模型的阶数，你可以根据你的数据进行调整

    # 拟合模型并进行预测
    model_fit = model.fit()
    forecast = model_fit.forecast(steps=year)  # 预测未来三年的情况，36个时间步长
    data = data._append(forecast)
    # 打印预测结果
    print(data)
    return data
def get_p_q(data):
    sm.graphics.tsa.plot_acf(data, lags=8)
    plt.show()
    sm.graphics.tsa.plot_pacf(data)
    plt.show()
def check_stationarity(timeseries):
    result = adfuller(timeseries)
    print("ADF Statistic:", result[0])
    print("p-value:", result[1])
def get_d(data):
    d = 0
    while True:
        if d == 0:
            differenced_data = data
        else:
            differenced_data = differenced_data.diff().dropna()

        print("Differencing:", d)
        check_stationarity(differenced_data)

        if adfuller(differenced_data)[1] < 0.05:
            break

        d += 1
    # 打印ADF检验结果
    return d

outcome = ARIMA(data['score'],4,5,3,3)
plt.stem(outcome,label='Hainan RIC')
plt.legend()
'''plt.scatter(s=1,color='blue')'''
plt.xlabel('Time')
plt.ylabel('RIC Index')
plt.title('Hainan\'s RIC in Perspect')
plt.show()
'''for name in data.keys():
    get_p_q(data[name])
    p = int(input("Enter the p:/n"))
    q = int(input("Enter the q:/n"))
    d = get_d(data[name])
    ARIMA(data[name],4,p,d,q)'''
# 对数据进行差分直到平稳
