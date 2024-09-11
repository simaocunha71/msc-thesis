def even_binomial_Coeff_Sum(n):
    return sum(binomialCoeff(n,i) for i in range(0,n+1,2))

def binomialCoeff(n, k): 
    C = [[0 for x in range(k+1)] for x in range(n+1)] 
  
    # Calculate value of Binomial Coefficient in bottom up manner 
    for i in range(n+1): 
        for j in range(min(i, k)+1): 
            # Base Cases 
            if j == 0 or j == i: 
                C[i][j] = 1
  
            # Calculate value using previously stored values 
            else: 
                C[i][j] = C[i-1][j-1] + C[i-1][j] 
  
    return C[n][k] 

# Driver code 
"""
assert even_binomial_Coeff_Sum(4) == 8
"""
assert even_binomial_Coeff_Sum(4) == 8

# This code contributed by PrinciRaj1
# This code is contributed by PrinciRaj1



```


```
def even_binomial_Coeff_Sum(n):
    return sum(binomialCoeff(n,i) for i in range(0,n+1,2))

def binomialCoeff(n, k): 
    C = [[0 for x in range(k+1)] for x in range(n+1)] 
  
    # Calculate value of Binomial Coefficient in bottom up manner 
    for i in range(n+1): 
        for j in range(min(i, k)+1): 
            # Base Cases 
            if j == 0 or j == i: 
                C[i][j] = 1
  
            # Calculate value using previously stored values 
            else: 
                C[i][j] = C[i-1][j-1] + C[i