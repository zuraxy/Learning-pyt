myUniqueList = []
myLeftovers = []
#print(myUniqueList)

#myUniqueList.append("x")
#print(myUniqueList)


def func(x,y):
    myUniqueList.append(x)
    if x == y:
        print("false")    
        def func1(y):
            myLeftovers.append(y)
            print(myLeftovers)
        func1(y)
    else:
        myUniqueList.append(y)
        print("True")
    return func

func(2,2)
print(myUniqueList)