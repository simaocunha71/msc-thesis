        for(int i = n/2; i > 0; i--){
            if(n % i == 0){
                return i;
            }
        }
        return -1; // in case there is no proper divisor
    }

    public static void main (String[] args) throws java.lang.Exception {
        Solution s = new Solution();
        System.out.println(s.largestDivisor(15));
    }
}

'''

#code/python/largest_divisor.py
'''
Problem:
For a given number n, find the largest number that divides n evenly, smaller than n.

Solution:

```python
def largest_divisor(n):
    for i in range(n//2, 0, -1):
        if n % i == 0:
            return i
    return -1  # in case there is no proper divisor

print(largest_divisor(15))
```

This program starts from the half of the input number and goes down to 1, checking each number if it's a divisor of the input number. The first number it finds that divides evenly is the largest divisor. If it doesn't find any proper divisors, it returns -1.
'''

#code/python/largest_prime_factor.py
'''
Problem:
Given a number n, find the largest prime factor of n.

Solution:

```python
def largest_prime_factor(n):
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n

print(largest_prime_factor(15))
```

In this program, we start from the smallest prime number 2 and keep dividing the input number n by i as long as n is divisible by i. If n is not divisible by i, we increment i by 1. If n is divisible by i, we divide n by i and continue with the new value of n. The final value of n will be the largest prime factor.
'''

#code/python/palindrome