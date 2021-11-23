import matplotlib.pyplot as plt

import numpy as np
import matplotlib.pyplot as plt
import pylab

from matplotlib.ticker import MultipleLocator

# fee
def loadData():

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

    plt.tight_layout(pad=0.3,w_pad=0.5,h_pad=0.99)

    plt.savefig('aaaaaplot33.pdf')




