# main file for solver that interacts with user
import math
import csv
import time
from print_sudoku import *

from sudoku_solver import solve

input_file=input("Input the path to csv file : ")               # input file must be in test_cases folder
use_dia=0
try:
    use_dia=int(input("Do you want to use Diagonal constraint(Specify 1/0) : "))
except:
    print("Invalid value setting to 0")
k=-1
rows=[]

# take input from csv file
try:
    with open("test_cases/"+input_file,'r') as csvfile:
        csvreader=csv.reader(csvfile)
        for row in csvreader:
            row_int=[]
            for element in row:
                row_int.append(int(element))
            rows.append(row_int)
    k=int(math.sqrt(len(rows)/2))
    print("INPUT:")
    print_main(rows,k)                                          # print the input
except :
    print("\nWrong csv file")
    exit()

print("\nOUTPUT:")
#Checking input
for row in rows:
    for ele in row:
        if ele>k*k:
            print("Wrong Input")
            exit()

start_time=time.time()
result=solve(rows,k,True if use_dia==1 else False)              # solve the sudoku
end_time=time.time()

if result :
    print_main(result,k)                                        # print the output
else:
    print("None")
print("\nTime Taken: "+str(end_time-start_time)+"s")