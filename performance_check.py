# python file to print time taken for various values of k
from sudoku_generator import gen
from sudoku_solver import solve
import time

k_i=int(input("Input k value till which program should run : "))

print("Result:")

input_file=""
for k in range(3,k_i+1):    
    with open("Performance_log.txt","a") as per_file:
        s="k="+str(k)+":\t"
        per_file.write(s)
        print(s,end="")
        
        st_time=time.time()
        rows=gen(k,False)
        end_time=time.time()
        s="Generator: "+str(round(end_time-st_time,2))+"s\t"
        per_file.write(s)
        print(s,end="")
        
        st_time=time.time()
        solve(rows,k,False)
        end_time=time.time()
        s="Solver: "+str(round(end_time-st_time,2))+"s\n"
        per_file.write(s)
        print(s,end="")
        
