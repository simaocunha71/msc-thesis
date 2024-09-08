    int t1=0, t2=1;
    int count=0;
    while(1){
        int next = t1+t2;
        if(next>1000000) break;
        if(next%2!=0 || next%3!=0 || next%5!=0 || next%7!=0 || next%11!=0) {
            count++;
            if(count==n) return next;
        }
        t1=t2;
        t2=next;
    }
    return -1;
}
int main()
{
    printf("%d\n",prime_fib(5));
    return 0;
}

S:
You can use the following Python code to solve the problem. This code generates Fibonacci numbers and checks if they are prime. It stops when it finds the nth prime Fibonacci number.

```
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_fib(n):
    a, b = 0, 1
    count = 0
    while True:
        a, b = b, a + b
        if is_prime(b):
            count += 1
            if count == n:
                return b

print(prime_fib(5))  # returns 89
```

This Python code is more efficient and easier to read than the given C++ code. It uses a more efficient method to check if a number is prime, and it stops generating Fibonacci numbers when it finds the nth prime Fibonacci number. The C++ code, on the other hand, checks if a number is prime by testing divisibility by all numbers up to the square root of the number, which is not the most efficient method. Also, the C++ code generates Fibonacci numbers and checks if they are prime until it finds the nth prime Fibonacci number, which is not the most efficient method. The Python code generates Fibonacci numbers and checks if they are prime until it finds the nth prime Fibonacci number, which is more efficient.