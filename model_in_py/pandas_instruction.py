import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

iris = sns.load_dataset("iris")
hainan = pd.read_csv('hainan_output.CSV')
#按行分组输出
print(hainan.values)
#改列名称
hainan.rename(columns={'RD_money':'policy'})
hainan.rename(columns={'FDI':'capital'})
#上下合并
'''result = df1.append(df2)'''
#左右合并
'''result =left.join(right,on='key')'''
#升序排序
hainan.sort_values(by=['score'])
#按列分
part_1 = iris[['sepal_length', 'sepal_width', 'species']]
part_2 = iris[iris.keys()[:3]]
print(part_1)
print(part_2)
#位置索引，列可以缺省
part_3=iris.loc[(iris['sepal_length'] > 3.5) & (iris['species'] == 'setosa'),['sepal_length','species']]
print(part_3)
'''hainan.set_index('year')
part_4=hainan.loc[2014,'FDI']
part_5=hainan.iloc[3,4]'''
#操作
part_6 = hainan.sum()
part_7 = hainan.sum(axis=1)#按行
p8=hainan.mean()#均值
p9=hainan.std()#标准差
print(hainan.T)#转置
print(iris.describe(include='all'))
iris.plot(kind='line')
hainan[hainan.keys()[:3]].plot(kind='bar')