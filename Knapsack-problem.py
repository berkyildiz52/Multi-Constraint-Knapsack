def readData(fileName):
    f = open(fileName, "r")
    #read the m and n values
    nK,nI=f.readline().split()
    nI=int(nI)
    nK=int(nK)
    #read all values
    if (nI%10==0):
        loopI=nI//10
    else:
        loopI=(nI//10)+1
    v=[]
    for i in range(loopI):
        v.extend(f.readline().split())
    c=map(int,v)
    v=list(c)
    w=[0]*len(v)
    #reading Knapsack capacity
    if (nK%10==0):
        loopI=nK//10
    else:
        loopI=(nK//10)+1
    knapsack_capacity=[]
    for i in range(loopI):
        knapsack_capacity.extend(f.readline().split())
    c=map(int,knapsack_capacity)
    knapsack_capacity=list(c)

    knapsack_weights=[]
    if (nI% 10 == 0):
        loopI = nI // 10
    else:
        loopI = (nI // 10) + 1


    for i in range(nK):
        l = []
        for j in range(loopI):
             l.extend(f.readline().split())
        c=map(int,l)
        l=list(c)
        knapsack_weights.append(l)




    return nK,v,w,knapsack_weights,knapsack_capacity
def findMax(l):
    return max(l), l.index(max(l))
def ifZero(l):
    for i in l:
        if i==0:
            return False
    return True

def findMin(l):
    return min(l), l.index(min(l))
def removeWight(l,index):
    for i in l:
        i[index].remove()
def knapsackTotal(knapsackNum,values,resultList,knapsackWeights,knapsackCapacity):
    check = True
    total = 0
    count=0
    #loop will work until any of the knasackcapacities reached zero or the list of the values is empty
    while (ifZero(knapsackCapacity)and count<len(values)):
        #get the largetest value and remove it from the list of values
        x, index = findMax(values)
        values[index]=0
        #chaeck all the knapsacks capacities and make sure that adding the value will not execed the limit
        for i in range(knapsackNum):
            if knapsackCapacity[i] - knapsackWeights[i][index] < 0:
                check = False
            else:
                #if it will not execed the capacity substract the wight from the knapsack capacity
                knapsackCapacity[i] -= knapsackWeights[i][index]
        #if the check if true add value to the total and replace the zero in the results list to 1

        if check:
            total += x
            resultList[index] = 1
        count+=1
    return total,resultList
def saveOutput(total,resultList):
    f = open("output.txt", "w")
    f.write(str(total) + '\n')
    for i in resultList:
        f.write(str(i) + '\n')
    f.close()



fileName=input('enter the file name.txt')
#read data from input files
knapsack_number,values,resultsList,knapsack_weights,knapsack_capacity=readData(fileName)
print(len(knapsack_weights[1]))
print(knapsack_weights,knapsack_capacity)


#calculate the Knapsack total
total,resultsList=knapsackTotal(knapsack_number,values,resultsList,knapsack_weights,knapsack_capacity)
#save results in file
saveOutput(total,resultsList)
print(total)







