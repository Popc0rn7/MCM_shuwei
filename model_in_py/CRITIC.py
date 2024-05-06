import numpy as np
import pandas as pd

def critic(X):
    n,m = X.shape
    X=np.array(X)
    #X = min_best(X)  # 自己的数据根据实际情况
    #Z = standard(X)  # 标准化X，去量纲
    R = np.array(pd.DataFrame(X).corr())
    #print(R)
    delta = np.zeros(m)
    c = np.zeros(m)
    for j in range(0,m):
        delta[j] = X[:,j].std()
        c[j] = R.shape[0] - R[:,j].sum()
    C = delta * c
    print(C)
    w = C/sum(C)
    return np.round(w,3)

def min_best(X):
    for k in X.keys():
        X[k] = max(X)-X[k]
    return X

def standard(X):
    xmin = X.min(axis=0)
    xmax = X.max(axis=0)
    xmaxmin = xmax-xmin
    n, m = X.shape
    for i in range(n):
        for j in range(m):
            X[i,j] = (X[i,j]-xmin[j])/xmaxmin[j]
    return X

if __name__ == '__main__':
    '''X=np.array([[0.4830,13.2682,0.0000,4.3646,5.1070],
    [0.4035,13.4909,39.0131,3.6151,5.5005],
    [0.8979,25.7776,9.0513,4.8920,7.5342],
    [0.5927,16.0245,13.2935,4.4529,6.5913]])'''
    X = pd.read_csv('hainan.csv', index_col=0)
    print(X)
    print(critic(X))
