import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
data = pd.read_csv('Hainan.CSV')
data = data[['industry','GDP','FDI']]
def kmeans(data, num_data, m, num_center, ax):
    # 获取4个随机数
    data = np.array(data)
    rarray = np.random.random(size=num_center)
    # 乘以数据集大小——>数据集中随机的4个点
    rarray = np.floor(rarray * num_data)
    # 转为int
    rarray = rarray.astype(int)
    print('数据集中随机索引', rarray)
    # 随机取数据集中的4个点作为初始中心点
    center = data[:, :-1][rarray]
    # 测试比较偏、比较集中的点，效果依然完美，测试需要删除以上代码
    # center = np.array([[4.6,-2.5],[4.4,-1.7],[4.3,-0.7],[4.8,-1.1]])
    # 1行80列的0数组，标记每个样本所属的类(k[i])
    cls = np.zeros([num_data], np.int64)
    print('初始center=\n', center)
    run = True
    time = 0
    while run:
        time = time + 1
        for i in range(num_data):
            # 求差
            tmp = data[:, :-1][i] - center
            # 求平方
            tmp = np.square(tmp)
            # axis=1表示按行求和
            tmp = np.sum(tmp, axis=1)
            # 取最小（最近）的给该点“染色”（标记每个样本所属的类(k[i])）
            cls[i] = np.argmin(tmp)
        # 如果没有修改各分类中心点，就结束循环
        run = False
        # 计算更新每个类的中心点
        for i in range(num_center):
            # 找到属于该类的所有样本
            club = data[:, :-1][cls==i]
            # axis=0表示按列求平均值，计算出新的中心点
            newcenter = np.mean(club, axis=0)
            # 如果新旧center的差距很小，看做他们相等，否则更新之。run置true，再来一次循环
            ss = np.abs(center[i]-newcenter)
            if np.sum(ss, axis=0) > 1e-5:
                center[i] = newcenter
                run = True
        print('new center=\n', center)
    print('程序结束，迭代次数：', time)
    # 按类打印图表，因为每打印一次，颜色都不一样，所以可区分出来
    for i in range(num_center):
        club = data[cls == i]
        print(club)
        print('next club')
        showtable(club, ax)
    # 打印最后的中心点
    #showtable(center, plt)


def showtable(data, ax):
    x = data.T[0]
    y = data.T[1]
    z = data.T[2]
    ax.scatter(x, y, s=z, alpha=0.8)


if __name__ == "__main__":
    #iris_set = sns.load_dataset('iris')

    fig, ax = plt.subplots()

    ax.set_xlabel('FDI', fontsize=15)
    ax.set_ylabel('RIC_index', fontsize=15)
    ax.set_title('RIC and FDI')

    ax.grid(True)
    fig.tight_layout()
    # 打印原始数据
    # showtable(csv.values, plt)
    kmeans(data, 9, 2, 4, ax)
    plt.show()

'''下面是数据集KmeansData.txt

x,y
1.658985,4.285136
-3.453687,3.424321
4.838138,-1.151539
-5.379713,-3.362104
0.972564,2.924086
-3.567919,1.531611
0.450614,-3.302219
-3.487105,-1.724432
2.668759,1.594842
-3.156485,3.191137
3.165506,-3.999838
-2.786837,-3.099354
4.208187,2.984927
-2.123337,2.943366
0.704199,-0.479481
-0.392370,-3.963704
2.831667,1.574018
-0.790153,3.343144
2.943496,-3.357075
-3.195883,-2.283926
2.336445,2.875106
-1.786345,2.554248
2.190101,-1.906020
-3.403367,-2.778288
1.778124,3.880832
-1.688346,2.230267
2.592976,-2.054368
-4.007257,-3.207066
2.257734,3.387564
-2.679011,0.785119
0.939512,-4.023563
-3.674424,-2.261084
2.046259,2.735279
-3.189470,1.780269
4.372646,-0.822248
-2.579316,-3.497576
1.889034,5.190400
-0.798747,2.185588
2.836520,-2.658556
-3.837877,-3.253815
2.096701,3.886007
-2.709034,2.923887
3.367037,-3.184789
-2.121479,-4.232586
2.329546,3.179764
-3.284816,3.273099
3.091414,-3.815232
-3.762093,-2.432191
3.542056,2.778832
-1.736822,4.241041
2.127073,-2.983680
-4.323818,-3.938116
3.792121,5.135768
-4.786473,3.358547
2.624081,-3.260715
-4.009299,-2.978115
2.493525,1.963710
-2.513661,2.642162
1.864375,-3.176309
-3.171184,-3.572452
2.894220,2.489128
-2.562539,2.884438
3.491078,-3.947487
-2.565729,-2.012114
3.332948,3.983102
-1.616805,3.573188
2.280615,-2.559444
-2.651229,-3.103198
2.321395,3.154987
-1.685703,2.939697
3.031012,-3.620252
-4.599622,-2.185829
4.196223,1.126677
-2.133863,3.093686
4.668892,-2.562705
-2.793241,-2.149706
2.884105,3.043438
-2.967647,2.848696
4.479332,-1.764772
-4.905566,-2.911070'''