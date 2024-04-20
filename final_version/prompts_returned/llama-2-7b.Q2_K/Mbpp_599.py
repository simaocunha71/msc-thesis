"""
Write a function to find sum and average of first n natural numbers.
assert sum_average(10)==(55, 5.5)
"""

def sum_average(n):
    # write your code here

    if n == 0: return (0, 0.)
    
    total = 0; avg = 0
    for i in range(1, n + 1):
        total += i
    print("The sum of the first "+ str(n) + " natural number is " + str(total))
    print("The average of the first "+str(n)+"natural number is " + str(total/float(i-1)))
    
    return (total, float(i-1)/total)

if __name__=="__main__":
    print("sum_average(10)")
    n = int(input())
    sum_average(n)