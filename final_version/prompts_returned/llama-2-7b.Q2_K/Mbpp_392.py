"""
Write a function to find the maximum sum possible by using the given equation f(n) = max( (f(n/2) + f(n/3) + f(n/4) + f(n/5)), n).
assert get_max_sum(60) == 106
"""
import math

def get_max_sum(n):
    '''
      find the maximum sum possible by using the given equation 
      f(n)= max (f(n/2), f(n/3), f(n/4), f(n/5)), n)
    '''
    
    if n==0: return 0
    lis = []
    
    for i in range(1,int(math.sqrt(n))+1):
        temp= (f(i/2)+f(i/3)+f(i/4)+f(i/5))#get sum of f(n/2),f(n/3),f(n/4),f(n/5) for n=n
        
        if i not in lis:
            if temp>0 and temp<n:
                lis.append(i)
    return max(lis)
    
    # output the highest sum possible
if __name__=='__main__':
    print get_max_sum(126)