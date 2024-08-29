def count_Primes_nums(n):
    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1
    prime[0]= False
    prime[1]= False
    return prime.count(True)

print(count_Primes_nums(5))

#Time complexity: O(n log log n)
#Space complexity: O(n)
<jupyter_output>
2
<jupyter_text>
**Question 10**Given a list of numbers, write a python function that returns a new list with only the prime numbers.
<jupyter_code>
