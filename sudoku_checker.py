#checks all .csv files in test_cases for invalid sudokus
import csv
import glob
import math

def isValidSudoku(rows,k):
    #column check
    for i in range(k*k):
        col=set()
        for j in range(k*k):
            if rows[i][j]==0:
                continue
            if rows[i][j] in col :
                return False
            else:
                col.add(rows[i][j])
    
    #row check
    for j in range(k*k):
        row=set()
        for i in range(k*k):
            if rows[i][j]==0:
                continue
            if rows[i][j] in row :
                return False
            else:
                row.add(rows[i][j])
                
    #block check
    for ni in range(0,k,k):
        for nj in range(0,k,k):
            block=set()
            for i in range(ni,ni+k):
                for j in range(nj,nj+k):
                    if rows[i][j]==0:
                        continue
                    if rows[i][j] in block:
                        return False
                    else:
                        block.add(rows[i][j])
    return True

def ValidPair(row1,row2,k):
    #respective cell check
    for i in range(k*k):
        for j in range(k*k):
            if rows[i][j]==0:
                continue
            if row1[i][j]==row2[i][j]:
                return False
    
    return isValidSudoku(row1,k) and isValidSudoku(row2,k)

l=glob.glob("test_cases/*.csv")
for file in l:
    rows=[]
    with open(file,'r') as csvfile:
        csvreader=csv.reader(csvfile)
        for row in csvreader:
            row_int=[]
            for element in row:
                row_int.append(int(element))
            rows.append(row_int)
    k=int(math.sqrt(len(rows)/2))
    row1=[]
    row2=[]
    for i in range(0,2*k*k):
        if i<k*k:
            row1.append(rows[i])
        else:
            row2.append(rows[i])
    if not ValidPair(row1,row2,k):
        print("Invalid file :"+file)
print("All files check complete!")
    
