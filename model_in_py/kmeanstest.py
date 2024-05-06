import numpy as np
import matplotlib.pyplot as plt
import pandas_instruction as pd
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