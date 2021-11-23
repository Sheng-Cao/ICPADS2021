import random

#Node selection for different schemes

if __name__ == '__main__':
    worknum = 300
    allround = 305
    while worknum < allround:
        #print(random.randint(0, 9) * 100)
        i = 0
        j = 0
        round = 10
        while j < round:
            i = 0
            li = []
            li = [0] * worknum
            #print(i)
            while i < worknum:
                # y = random.random()
                # li.append((random.random())
                li[i] = random.random()
                i = i + 1
            print(li)
            lis = sorted(li)
            print(lis)
            print(lis[1])
            #the selection process of reverse Vickrey auction 
            winnerfile = 'round10/aaawinner'+str(worknum)
            f = open(winnerfile, 'a+')
            f.write(str(lis[1]) + "\n")
            f.flush()
            #the random selection process
            randomchoicefile = 'round10/aaarandomchoice' + str(worknum)
            randomchoice = random.randint(0, worknum-1)
            print(randomchoice)
            f = open(randomchoicefile, 'a+')
            f.write((str(li[randomchoice]) + "\n"))
            j = j + 1
            f.flush()

        worknum=worknum+1

    # f = open(r'suiji', 'w+')
    #
    # while i < 100:
    #     y = random.random()
    #     #print(y)
    #
    #     f.write(str(y) + "\n")
    #     f.flush()
    #     i = i + 1
    #
    # li = []
    # with open('suiji', 'r') as op:
    #     for line in op:
    #         lin = line
    #         li.append(line.strip())
    # print(li)
    # print(111111111111111)
    # lis = sorted(li)
    # print(lis)

    # f = open(r'paixu', 'w+')
    # while i < 10:
    #     m = lis[i]
    #     f.write(str(m) + "\n")
    #     f.flush()
    #     i = i + 1
    print_hi('PyCharm')

