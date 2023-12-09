
def tri(n):
    """Everyone knows Fibonacci sequence, it was studied deeply by mathematicians in 
    the last couple centuries. However, what people don't know is Tribonacci sequence.
    Tribonacci sequence is defined by the recurrence:
    tri(1) = 3
    tri(n) = 1 + n / 2, if n is even.
    tri(n) =  tri(n - 1) + tri(n - 2) + tri(n + 1), if n is odd.
    For example:
    tri(2) = 1 + (2 / 2) = 2
    tri(4) = 3
    tri(3) = tri(2) + tri(1) + tri(4)
           = 2 + 3 + 3 = 8 
    You are given a non-negative integer number n, you have to a return a list of the 
    first n + 1 numbers of the Tribonacci sequence.
    Examples:
    tri(3) = [1, 3, 2, 8]
    """
    
    if n == 0 or n < 0 :
        raise ValueError("n must be non-negative, but you have entered an invalid input.")
        
    n_list = []
    i = 0
    while (i<n): # Loop to create a sequence for all numbers upto "n"
        if ((i+1)%2 == 1): 
            t = tri(i + 1)
            
            if (t < 3):  
                print(str(tri(i)), end=' ')
                n_list.append(tri(i))    
            else:
                print(str(tri(i)), end=' ')
                t = tri(i - 1)                
        elif ((i+1)%2 == 0):
            if (i > n-4 and i < n+3):
                print(str(tri(i)), end=' ')
                n_list.append(tri(i))    
            elif (i != -1 and i < n + 4):                          #If we are returning less than 5 elements