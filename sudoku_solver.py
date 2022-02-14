from pysat.solvers import Solver
from pysat.card import *
from pysat.formula import CNF
import math

#extracts a sudoku solution(in list of list format) from given model
def get_ans(model,ans,k):
    model=[ele for ele in model if ele>0]
    fac=10**(int(math.log10(k*k)+1))
    for i in model:
        value=i%fac
        i=int(i/fac)
        y=int(i%fac)
        i=int(i/fac)
        x=int(i%fac)
        n=int(i/fac)-1
        ans[x+k*k*n][y]=value
    return ans

# return assumptions from a partially filled sudoku
def assume_gen(rows,k):
    assume=[]
    fac=10**(int(math.log10(k*k)+1))
    
    for i in range(0,2*k*k):
        for j in range(0,k*k):
            if(rows[i][j]!=0):
                assume.append( (int(i/(k*k))+1)*(fac**3) 
                              + (i%(k*k))*fac*fac 
                              + j*fac 
                              + rows[i][j] )
    
    return assume

# formula generator for solving sudoku
# uses a variable x({1,2})(row no.)(col no.)(value)
def formula_gen(k,use_dia):
    cnf=CNF()
    fac=10**(int(math.log10(k*k)+1))        # factor by which row no., col no., value will be separated
    
    # Each cell must have only one value from 1 to k*k for both S1, S2
    for i in range(0,k*k):
        for j in range(0,k*k):
            l1=[]
            l2=[]
            for z in range(1,k*k+1):
                l1.append(fac**3+i*fac*fac+j*fac+z)
                l2.append(2*fac**3+i*fac*fac+j*fac+z)
            cnf.extend(CardEnc.equals(lits=l1,bound=1,encoding=0))
            cnf.extend(CardEnc.equals(lits=l2,bound=1,encoding=0))
            
    # each sub-block must have only one occurance of every number from 1 to k*k
    for ni in range(0,k):                                               # selects sub-block row
        for nj in range(0,k):                                           # selects sub-block column 
                       
            for n in range(1,k*k+1):                                    # selects a number from 1 to k*k
                l1=[]
                l2=[]
                for i in range(ni*k,ni*k+k):                            # selects row of cell in that sub-block
                    for j in range(nj*k,nj*k+k):                        # selects column of cell in that sub-block
                        l1.append(fac**3+i*fac*fac+j*fac+n)
                        l2.append(2*fac**3+i*fac*fac+j*fac+n)
                cnf.extend(CardEnc.equals(lits=l1,bound=1,encoding=0))
                cnf.extend(CardEnc.equals(lits=l2,bound=1,encoding=0))

    # each column must have exactly one occurance of each number from 1 to k*k
    for i in range(0,k*k):
        for z in range(1,k*k+1):
            l1=[]
            l2=[]
            for j in range(0,k*k):
                l1.append(fac**3+i*fac*fac+j*fac+z)
                l2.append(2*fac**3+i*fac*fac+j*fac+z)
            cnf.extend(CardEnc.equals(lits=l1,bound=1,encoding=0))
            cnf.extend(CardEnc.equals(lits=l2,bound=1,encoding=0))
    
    # each row must have exactly one occurance of each number from 1 to k*k
    for j in range(0,k*k):
        for z in range(1,k*k+1):
            l1=[]
            l2=[]
            for i in range(0,k*k):
                l1.append(fac**3+i*fac*fac+j*fac+z)
                l2.append(2*fac**3+i*fac*fac+j*fac+z)
            cnf.extend(CardEnc.equals(lits=l1,bound=1,encoding=0))
            cnf.extend(CardEnc.equals(lits=l2,bound=1,encoding=0))

    # Corresponding cells in S1, S2 must not be equal. Atmost one is possible.
    for i in range(0,k*k):
        for j in range(0,k*k):
            for z in range(1,k*k+1):
                cnf.extend(CardEnc.atmost([ fac**3+i*fac*fac+j*fac+z , 2*fac**3+i*fac*fac+j*fac+z ],encoding=0))
    
    # Want to use diagonal consraint or not
    if use_dia :
        # Diagonal elements should have all numbers from 1 to k*k
        for n in range(k*k+1):
            l1=[]
            l2=[]
            for i in range(k*k):
                l1.append(fac**3+i*fac*fac+i*fac+n)
                l2.append(2*fac**3+i*fac*fac+i*fac+n)
            cnf.extend(CardEnc.equals(lits=l1,bound=1,encoding=0))
            cnf.extend(CardEnc.equals(lits=l2,bound=1,encoding=0))
        
        # Anti-Diagonal elements should have all numbers from 1 to k*k
        for n in range(k*k+1):
            l1=[]
            l2=[]
            for i in range(k*k):
                l1.append(fac**3+i*fac*fac+(k*k-i-1)*fac+n)
                l2.append(2*fac**3+i*fac*fac+(k*k-i-1)*fac+n)
            cnf.extend(CardEnc.equals(lits=l1,bound=1,encoding=0))
            cnf.extend(CardEnc.equals(lits=l2,bound=1,encoding=0))
    
    return cnf

#main function that receives request to solve sudoku(rows) with k=k
def solve(rows,k,use_dia):
    cnf=formula_gen(k,use_dia)                              #generates formula for solving sudoku
    
    s=Solver(name='m22')
    s.append_formula(cnf.clauses)
    
    solved=s.solve(assumptions=assume_gen(rows,k))
    
    if solved:
        model=s.get_model()
        ans=get_ans(model,rows,k)
        s.delete()
        return ans
    else:
        s.delete()
        return None

