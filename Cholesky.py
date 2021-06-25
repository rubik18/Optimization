'''
Created on Oct 19, 2020

@author: ThamDinh
'''
# Python3 program to decompose  
# a matrix using Cholesky  
# Decomposition 
import math 
MAX = 100; 
  
def Cholesky_Decomposition(matrix, n): 
  
    lower = [[0 for x in range(n + 1)]  
                for y in range(n + 1)]; 
  
    # Decomposing a matrix 
    # into Lower Triangular 
    for i in range(n):  
        for j in range(i + 1):  
            sum1 = 0; 
  
            # sum1mation for diagnols 
            if (j == i):  
                for k in range(j): 
                    sum1 += pow(lower[j][k], 2); 
                lower[j][j] = math.sqrt(matrix[j][j] - sum1); 
            else: 
                  
                # Evaluating L(i, j) 
                # using L(j, j) 
                for k in range(j): 
                    sum1 += (lower[i][k] *lower[j][k]); 
                if(lower[j][j] > 0): 
                    lower[i][j] = (matrix[i][j] - sum1) / lower[j][j]; 
  
    # Displaying Lower Triangular 
    # and its Transpose 
    print("Ma trận L\t\t\t Ma trận Lt"); 
    for i in range(n):  
          
        # Lower Triangular 
        for j in range(n): 
            print(lower[i][j], end = "\t"); 
        print("", end = "\t"); 
          
        # Transpose of 
        # Lower Triangular 
        for j in range(n): 
            print(lower[j][i], end = "\t"); 
        print(""); 
  
# Driver Code 
n = 3; 
matrix = [[4.0, -1.0, 1.0], 
          [-1.0, 4.25, 2.75], 
          [1.0, 2.75, 3.5]]; 
Cholesky_Decomposition(matrix, n); 
  
# This code is contributed by mits 