def func(row,column):
    for row in range(0,row):
        if (row%2 == 0):
            for col in range(0,column+1):
                if (col%2 == 0) and (col == column):
                    print("")
                elif (col%2 == 1) and (col == column):
                    print("")
                elif (col%2 == 1) and (col != column):
                    print("|",end="")
                elif (col%2 == 0) and (col != column):
                    print(" ",end="")
        else:
            for col in range(0,column+1):
                if (col != column):
                    print("-",end="")
                else:
                    print("")
    if (column>216) or (row>50):
        print("False")
    else:
        print("True")
func(5,5)