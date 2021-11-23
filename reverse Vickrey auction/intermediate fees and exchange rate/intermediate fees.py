import matplotlib.pyplot as plt  

import numpy as np
import matplotlib.pyplot as plt
import pylab

def loadData():
    #inFile = open(flieName, 'r')  # 以只读方式打开某fileName文件
    # 定义两个空list，用来存放文件中的数据
    a = 2
    X = []
    Y = []
    while a < 303:
        X.append(a)

        lin = 0.00000000

        filenum='round10/aaawinner'+str(a)
        with open(filenum, 'r') as op:
            for line in op:
                lin =lin + float(line)
            lin=lin/10
            Y.append(lin)
            print(lin)
        a = a + 25

    return (X, Y)  # X,y组成一个元组，这样可以通过函数一次性返回

def loadData1():
    # inFile = open(flieName, 'r')  # 以只读方式打开某fileName文件
    # 定义两个空list，用来存放文件中的数据
    X1 = []
    Y1 = []
    a = 2
    while a < 303:
        X1.append(a)
        lin = 0.00000000
        ranflie='round10/aaarandomchoice'+str(a)
        with open(ranflie, 'r') as op:
            for line in op:
                lin = lin + float(line)
            lin = lin/10
            Y1.append(lin)
        a = a+25
    return (X1, Y1)  # X,y组成一个元组，这样可以通过函数一次性返回


# for line in inFile:
# trainingSet = line.split(',')  # 对于每一行，按','把数据分开，这里是分成两部分
# trainingSet = line.strip()
# Y.append(trainingSet)  # 第一部分，即文件中的第一列数据逐一添加到list X 中








if __name__ == '__main__':
    # X = np.linspace(-np.pi, np.pi, 256, endpoint=True)  # -π to+π的256个值
    # C, S = np.cos(X), np.sin(X)
    # plt.plot(X, C)
    # plt.plot(X, S)
    # # 在ipython的交互环境中需要这句话才能显示出来
    # plt.show()
    font_size = 50

    (X, Y) = loadData()
    (X1,Y1) = loadData1()
    plt.plot(X, Y, label = "based on Reverse Vickrey Auction", marker = "o")
    plt.plot(X1, Y1, label="Random Connector", marker = "x")
    plt.legend()
    pylab.xlabel('Number of nodes participating in the auction')
    pylab.ylabel('Intermediate fees for cross-chain transactions')
    #plt.plot(range(10))
    #plt.savefig('aaaaaplot11.pdf')
    # length = len(Y)
    # pylab.figure(1)
    # pylab.plot(X, Y,colorsys="black")
    # #plotData(X, Y)
    # #plotData(X1, Y1)

    pylab.show()
