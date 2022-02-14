import math

# main function that receives request to print (2*k*k X k*k) sudoku
def print_main(rows,k):
    num=int(math.log10(k*k))+1
    rows1=[]
    rows2=[]
    for i in range(0,2*k*k):
        if i<k*k :
            rows1.append(rows[i])
        else:
            rows2.append(rows[i])
    if(k>4):
        print("S1:")
        print_one(rows1,k)
        print("\nS2:")
        print_one(rows2,k)
    else:
        print("S1:",end="")
        for x in range(0,k*k*(num+1)+2*(k-1)):
            print(" ",end="")
        print("S2:")
        print_both(rows1,rows2,k)

# prints two sudokus single line
def print_both(rows1,rows2,k):
    num=int(math.log10(k*k))+1
    for i in range(0,k*k):
        if i!=0 and i%k==0:
            for x in range(0,k*k*(num+1)+2*k-1):
                print("-",end="")
            print("  ",end="")
            for x in range(0,k*k*(num+1)+2*k-1):
                print("-",end="")
            print("")
        for j in range(0,k*k):
            if j!=0 and j%k==0:
                print(" | "+ele(rows1[i][j],num),end="")
            else:
                print(" "+ele(rows1[i][j],num),end="")
        print("   ",end="")
        for j in range(0,k*k):
            if j!=0 and j%k==0:
                print(" | "+ele(rows2[i][j],num),end="")
            else:
                print(" "+ele(rows2[i][j],num),end="")

        print("")

# print one sudoku
def print_one(rows,k):
    num=int(math.log10(k*k))+1
    for i in range(0,k*k):
        if i!=0 and i%k==0:
            for x in range(0,k*k*(num+1)+2*k-1):
                print("-",end="")
            print("")
        for j in range(0,k*k):
            if j!=0 and j%k==0:
                print(" | "+ele(rows[i][j],num),end="")
            else:
                print(" "+ele(rows[i][j],num),end="")
        print("")

# return string after adding appropriate spaces in integer
def ele(x,num):
    s=str(x)
    c1= num-1 if x==0 else num-int(math.log10(x))-1
    for i in range(0,c1):
        s=" "+s
    return s



