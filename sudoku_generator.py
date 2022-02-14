# This file include core sudoku generator functions
import random
from pysat.solvers import Solver
from pysat.card import *
from sudoku_solver import solve,formula_gen,assume_gen

# This fills diagonal elements of empty sudokus S1, S2 randomly
def ran_fill(rows,k):
    for i in range(0,k):
        x=random.randint(1,k*k)
        rows[i*k][i*k]=x
        if k>1:
            y=random.randint(1,k*k)
            while y==x:
                y=random.randint(1,k*k)
            rows[(i+k)*k+k-1][i*k+k-1]=y

# This function checks if element at [x][y] can be removed (Uniqueness should not be disturbed)
def can_remove(rows,k,x,y):
    global s
    fac=10**(int(math.log10(k*k)+1))
    c1=rows[x][y]
    rows[x][y]=0
    assume=assume_gen(rows,k)
    for i in range(1,k*k+1):
        assume.append( (int(x/(k*k))+1)*(fac**3) 
                        + (x%(k*k))*fac*fac 
                        + y*fac 
                        + i )
        if i==c1:
            del assume[-1]
            continue
        elif s.solve(assumptions=assume):
            rows[x][y]=c1
            return False
        del assume[-1]
    rows[x][y]=c1
    return True

# This function removes random cells in a filled sudoku to maximal extent until it becomes impossible to maintain uniqueness
def remove(rows,k):
    x=list(range(0,2*k*k))
    y=list(range(0,k*k))
    random.shuffle(x)
    random.shuffle(y)
    
    for i in x:
        for j in y:
            
            if can_remove(rows,k,i,j):
                rows[i][j]=0

# main function of this script which fills a empty grid for valid sudoku, then start removing elements
def gen(k,use_dia):
    global s
    # assign a solver
    s=Solver(name="m22")
    s.append_formula(formula_gen(k,use_dia).clauses)
    # make a empty sudoku
    rows=[[0 for i in range(k*k)] for j in range(2*k*k)]
    
    ran_fill(rows,k)            #randomly fills sudoku's diagonal ele in S1, S2
    assume=assume_gen(rows,k)
    while not s.solve(assumptions=assume):    #fills till a valid sudoku is not formed
        ran_fill(rows,k)
        assume=assume_gen(rows,k)
    # print("random done")
    solve(rows,k,use_dia)
    remove(rows,k)
    return rows