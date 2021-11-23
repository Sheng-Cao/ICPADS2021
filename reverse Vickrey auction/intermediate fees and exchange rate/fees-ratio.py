import matplotlib.pyplot as plt  # 约定俗成的写法plt
# 首先定义两个函数（正弦&余弦）
import numpy as np
import matplotlib.pyplot as plt
import pylab
## 从.txt文件中读取数据
from matplotlib.ticker import MultipleLocator

# fee
def loadData():
    #inFile = open(flieName, 'r')  # To open a fileName file in read-only mode
    # Define two empty lists to hold the data in the file
    a = 3
    X = []
    Y = []
    while a < 301:
        X.append(a)

        lin = 0.00000000

        filenum='round1000/winner'+str(a)
        with open(filenum, 'r') as op:
            for line in op:
                lin =lin + float(line)
            lin=lin/100
            Y.append(lin)
            print(lin)
        a = a + 5

    return (X, Y) 

def loadData1():
    # inFile = open(flieName, 'r')  # To open a fileName file in read-only mode
    # Define two empty lists to hold the data in the file
    X1 = []
    Y1 = []
    a = 4
    while a < 301:
        X1.append(a)
        lin = 0.00000000
        ranflie='round1000/randomchoice'+str(a)
        with open(ranflie, 'r') as op:
            for line in op:
                lin = lin + float(line)
            lin = lin/100
            Y1.append(lin)
        a = a+1
    return (X1, Y1)  

# ratio
def loadData01():
    #inFile = open(flieName, 'r')  # To open a fileName file in read-only mode
    # Define two empty lists to hold the data in the file
    a = 2
    X = []
    Y = []
    while a < 103:
        X.append(a)

        lin = 0.00000000

        filenum='round10/aaawinner'+str(a)
        with open(filenum, 'r') as op:
            for line in op:
                lin =lin + float(line)
            lin=lin/10
            lin = (10-lin)/10
            #lin = 1/lin
            Y.append(lin)
            print(lin)
        a = a + 10

    return (X, Y)  
def loadData02():
    # inFile = open(flieName, 'r')  # To open a fileName file in read-only mode
    # Define two empty lists to hold the data in the file
    X1 = []
    Y1 = []
    a = 2
    while a < 103:
        X1.append(a)
        lin = 0.00000000
        ranflie='round10/aaarandomchoice'+str(a)
        with open(ranflie, 'r') as op:
            for line in op:
                lin = lin + float(line)
            lin = lin / 10
            lin = (10 - lin) / 10
            Y1.append(lin)
        a = a+10
    return (X1, Y1) 


if __name__ == '__main__':
    # X = np.linspace(-np.pi, np.pi, 256, endpoint=True)  # -π to+π的256个值
    # C, S = np.cos(X), np.sin(X)
    # plt.plot(X, C)
    # plt.plot(X, S)
    # plt.show()
    #font_size = 50
    plt.figure(figsize=(5, 6.5))
    (X, Y) = loadData()
    (X1,Y1) = loadData1()
    (X01, Y01) = loadData01()
    (X02, Y02) = loadData02()

    pylab.figure(1)
    ax1 = plt.subplot(211)
    plt.plot(X, Y, label = "based on Reverse Vickrey Auction")
    plt.plot(X1, Y1, label="Random Connector")
    pylab.xlabel('Node number')
    pylab.ylabel('Intermediate fees\n')
    plt.legend()

    ax2 = plt.subplot(212)
    plt.plot(X01, Y01, label="based on Reverse Vickrey Auction", marker="o")
    plt.plot(X02, Y02, label="Random Connector", marker="x")
    plt.legend()
    y_major_locator = MultipleLocator(0.05)
    ax = plt.gca()
    ax.yaxis.set_major_locator(y_major_locator)
    plt.ylim(0.76, 1.02)
    pylab.xlabel('Node number')
    pylab.ylabel('Ratio of the cross-blockchain exchange rate\n to the market exchange rate')
    plt.rcParams.update({"font.size": 20})  
    #ax1.set_title("(a) Intermediate Fees",y=-0.21,fontdict={'size':"15"})
    #ax2.set_title("(b) the exchange rate",y=-0.21,fontdict={'size':"15"})
    plt.tight_layout(pad=0.3,w_pad=0.5,h_pad=0.99)
    #plt.show()
    #plt.plot(range(10))
    plt.savefig('aaaaaplot33.pdf')
    # length = len(Y)
    # pylab.figure(1)
    # pylab.plot(X, Y,colorsys="black")
    # #plotData(X, Y)
    # #plotData(X1, Y1)

    #pylab.show()


# for line in inFile:
# trainingSet = line.split(',')  # 对于每一行，按','把数据分开，这里是分成两部分
# trainingSet = line.strip()
# Y.append(trainingSet)  # 第一部分，即文件中的第一列数据逐一添加到list X 中


## 绘制该文件中的数据
## 需要引入pylab库，里面用到的函数和MATLAB里的非常类似
# def plotData(X, Y):
#     length = len(Y)
#     pylab.figure(1)
#     pylab.plot(X,Y)
#     #pylab.plot(X[:10], Y[:10])
#     # pylab.plot(X[50], Y[50])
#     # pylab.plot(X[100], Y[100])
#     # pylab.plot(X[150], Y[150])
#     # pylab.plot(X[200], Y[200])
#     # pylab.plot(X[250], Y[250])
#
#     #pylab.plot(X, Y, 'rx')
#




