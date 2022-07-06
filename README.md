# Sudoku-Solver #
Following is the code of Sudoku Solver and Sudoku Generator written in Python using the **Pysat** library.

## 1. **Solver** : ##

   For solver run the following command
   ```
   python main_solver.py
   ```
   It will ask for input csv file. Provide name of csv in terminal. Eg. "abc.csv" (include extension)
    
   Then provide either 1(True) / 0(False) for diagonal constraint
    
   NOTE : csv file should be in `test_cases` folder

## 2. **Generator** : ##

   For generator run the following command
   ```
   python main_generator.py
   ```
   It will ask for input parameter k(k>1). Provide one integer in terminal.
    
   Then provide either 1(True) / 0(False) for diagonal constraint
    
   Then it will generate a parially filled maximal sudoku and its corresponding filled sudoku.
