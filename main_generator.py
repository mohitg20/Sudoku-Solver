# This script is to generate random sudoku pair
import time
import csv
from sudoku_generator import gen
from sudoku_solver import solve
from print_sudoku import *

# generate a random name for question and answer storage
file_name=str(int(time.time()))

# input value for k
k=-1
while k<2 :
    try :
        k=int(input("Provide a valid parameter k : "))
    except :
        print("Put correct value please")
        k=-1
use_dia=0
try:
    use_dia=int(input("Do you want to use Diagonal constraint(Specify 1/0) : "))
except:
    print("Invalid value setting to 0")

if(k>4):
    print("NOTE: Larger k values take time to execute. Please be patient.")
else :
    print("Please maximize your window for better view.")

# Solve the question generated and print it
start_time=time.time()
question=gen(k,True if use_dia==1 else False)
end_time=time.time()
print("Here is your generated sudoku pair:")
print_main(question,k)

# write question generated in test/ folder
with open("test_cases/"+str(k)+"_"+file_name+"_q.csv","w",newline="") as csvfile:
    csv.writer(csvfile).writerows(question)

# Solve the question generated and print it
solution=solve(question,k,True if use_dia==1 else False)
print("\nHere is its unique answer:")
print_main(solution,k)

# write solution generated in test/ folder
with open("test_cases/"+str(k)+"_"+file_name+"_s.csv","w",newline="") as csvfile:
    csv.writer(csvfile).writerows(solution)

# print the time taken
print("\nTime Taken for generation : "+str(end_time-start_time)+"s")