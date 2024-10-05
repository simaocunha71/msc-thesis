  if (n < 2) return false;

  for (let i = 2; i <= Math.sqrt(n); i++) {
    if (n % i === 0) return false;
  }

  return true;
}


A: Here is the python solution for the problem
def isPrime(n):
    if n < 2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

Here is how it works:

*

*If the number is less than 2 it is not prime so return False.

*If the number is 2 or more, check from 2 to the square root of the number.

*If the number is divisible by any of these numbers then it's not prime, so return False.

*If the number is not divisible by any of these numbers then it's prime, so return True.


A: Here is a JavaScript solution using a simple approach:


const isPrime = (num) => {
    if (num < 2) {
        return false;
    }
    for(let i = 2; i < num; i++) {
        if (num % i === 0) {
            return false;
        }
    }
    return true;
}

console.log(isPrime(13));  // Output: true
console.log(isPrime(15));  // Output: false


This function works by checking if any number from 2 to the given number (exclusive) evenly divides the given number. If it finds such a number, it returns false, because the number is not prime. If it doesn't find any such number, it returns true, because the number is prime.

A: Here is the Python solution for the problem:

```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

print(is_prime(6))  # Output: False
