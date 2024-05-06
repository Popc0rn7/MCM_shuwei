import pandas as pd
import numpy as np
import re


# 定义文件读取方法
'''def read_data(file):
    file_path = file
    raw_data = pd.read_excel(file_path, header=0)
    # print(raw_data)
    return raw_data'''


# 定义数据正向化、标准化方法
def data_normalization(data):
    data_nor = data.copy()
    columns_name = data_nor.columns.values
    for i in range((len(columns_name) - 1)):
        name = columns_name[i + 1]
        # print(name)
        # 正向指标直接标准化
        if ('Positive' in name) == True:
            max = data_nor[columns_name[i + 1]].max()
            min = data_nor[columns_name[i + 1]].min()
            data_nor[columns_name[i + 1]] = (data_nor[columns_name[i + 1]] - min) / (max - min)
            # print(data_nor[columns_name[i+1]])

        # 负向指标先正向化、在标准化
        if ('Negative' in name) == True:
            max0 = data_nor[columns_name[i + 1]].max()
            data_nor[columns_name[i + 1]] = (max0 - data_nor[columns_name[i + 1]])  # 正向化

            max = data_nor[columns_name[i + 1]].max()
            min = data_nor[columns_name[i + 1]].min()
            data_nor[columns_name[i + 1]] = (data_nor[columns_name[i + 1]] - min) / (max - min)  # 标准化
            # print(data_nor[columns_name[i+1]])

        # 适度指标先正向化、在标准化
        if ('Moderate' in name) == True:
            try:
                val_range = re.search(r'.*[\(（](.*),(.*)[\)）]', name)
                val_down = float(val_range.group(1))
                val_up = float(val_range.group(2))
                val_op = (val_up + val_down) / 2
            except:
                val_range = re.search(r'.*[\(（](.*)[\)）]', name)
                val_op = float(val_range.group(1))
            # print(val_op)
            data_nor[columns_name[i + 1]] = 1 - (abs(data_nor[columns_name[i + 1]] - val_op) / (
                abs(data_nor[columns_name[i + 1]] - val_op).max()))  # 正向化

            max = data_nor[columns_name[i + 1]].max()
            min = data_nor[columns_name[i + 1]].min()
            data_nor[columns_name[i + 1]] = (data_nor[columns_name[i + 1]] - min) / (max - min)  # 标准化
            # print(data_nor[columns_name[i+1]])

    # print(data_nor)
    return data_nor


# 定义计算熵权方法
def entropy_weight(data_nor):
    columns_name = data_nor.columns.values
    n = data_nor.shape[0]
    E = []
    for i in columns_name[1:]:
        # 计算信息熵
        # print(i)
        data_nor[i] = data_nor[i] / sum(data_nor[i])

        data_nor[i] = data_nor[i] * np.log(data_nor[i])
        data_nor[i] = data_nor[i].where(data_nor[i].notnull(), 0)
        # print(data_nor[i])
        Ei = (-1) / (np.log(n)) * sum(data_nor[i])
        E.append(Ei)
    # print(E)
    # 计算权重
    W = []
    for i in E:
        wi = (1 - i) / ((len(columns_name) - 1) - sum(E))
        W.append(wi)
    # print(W)
    return W


# 计算得分
def entropy_score(data, w):
    data_s = data.copy()
    columns_name = data_s.columns.values
    for i in range((len(columns_name) - 1)):
        name = columns_name[i + 1]
        data_s[name] = data_s[name] * w[i]
    return data_s


file = 'data.xls'  # 声明数据文件地址
data = read_data(file)  # 读取数据文件
data_nor = data_normalization(data)  # 数据标准化、正向化,生成标准化后的数据data_nor
W = entropy_weight(data_nor)  # 计算熵权权重
data_s = entropy_score(data, W)  # 计算赋权后的得分，使用原数据计算
data_nor_s = entropy_score(data_nor, W)

W.insert(0, '熵权法权重')  # 将结果保存为csv
W0 = pd.DataFrame(W).T
data_s.to_csv('熵权法得分结果(原始数据).csv', index=0)
W0.to_csv('熵权法得分结果(原始数据).csv', mode='a', header=False, index=0)
data_nor_s.to_csv('熵权法得分结果(标准化数据).csv', index=0)
W0.to_csv('熵权法得分结果(标准化数据).csv', mode='a', header=False, index=0)