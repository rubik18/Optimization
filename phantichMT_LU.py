'''
Created on Oct 19, 2020

@author: ThamDinh
'''
A = [[1,1,0,3],[2,1,-1,1],[3,-1,-1,2],[-1,2,3,-1]]
b = [1,1,-3,4]
# Python3 Program to decompose  
# a matrix into lower and 
# upper traingular matrix 
MAX = 100; 
  
def luDecomposition(mat, n): 
  
    lower = [[0 for x in range(n)]  
                for y in range(n)]; 
    upper = [[0 for x in range(n)]  
                for y in range(n)]; 
                   
    for i in range(n): 
  
        # Upper Triangular 
        for k in range(i, n):  
  
            # Summation of L(i, j) * U(j, k) 
            sum = 0; 
            for j in range(i): 
                sum += (lower[i][j] * upper[j][k]); 
  
            # Evaluating U(i, k) 
            upper[i][k] = mat[i][k] - sum; 
  
        # Lower Triangular 
        for k in range(i, n): 
            if (i == k): 
                lower[i][i] = 1; # Diagonal as 1 
            else: 
  
                # Summation of L(k, j) * U(j, i) 
                sum = 0; 
                for j in range(i): 
                    sum += (lower[k][j] * upper[j][i]); 
  
                # Evaluating L(k, i) 
                lower[k][i] = int((mat[k][i] - sum) /
                                       upper[i][i]); 
  
    # setw is for displaying nicely 
    print("Lower Triangular\t\tUpper Triangular"); 
  
    # Displaying the result : 
    for i in range(n): 
          
        # Lower 
        for j in range(n): 
            print(lower[i][j], end = "\t");  
        print("", end = "\t"); 
  
        # Upper 
        for j in range(n): 
            print(upper[i][j], end = "\t"); 
        print(""); 
  
# Driver code 
mat = [[1,1,0,3],[2,1,-1,1],[3,-1,-1,2],[-1,2,3,-1]]; 
  
luDecomposition(mat, 4); 
  
# This code is contributed by mits 
    