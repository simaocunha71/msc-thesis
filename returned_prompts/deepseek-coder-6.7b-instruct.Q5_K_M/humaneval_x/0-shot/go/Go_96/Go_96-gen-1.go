
    // 1. Create an empty array to store prime numbers
    primeNumbers := []int{}

    // 2. Create a function to check if a number is prime
    isPrime := func(num int) bool {
        if num < 2 {
            return false
        }
        for i := 2; i*i <= num; i++ {
            if num%i == 0 {
                return false
            }
        }
        return true
    }

    // 3. Iterate over the range from 2 to n
    for i := 2; i < n; i++ {
        // 4. Check if the number is prime
        if isPrime(i) {
            // 5. If the number is prime, append it to the primeNumbers array
            primeNumbers = append(primeNumbers, i)
        }
    }

    // 6. Return the primeNumbers array
    return primeNumbers
}

func main() {
    fmt.Println(CountUpTo(5))  //[2 3]
    fmt.Println(CountUpTo(11)) //[2 3 5 7]
    fmt.Println(CountUpTo(0))  //[]
    fmt.Println(CountUpTo(20)) //[2 3 5 7 11 13 17 19]
    fmt.Println(CountUpTo(1))  //[]
    fmt.Println(CountUpTo(18)) //[2 3 5 7 11 13 17]
}

```


## Python
```python
def CountUpTo(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    prime_numbers = [i for i in range(2, n) if is_prime(i)]
    return prime_numbers

print(CountUpTo(5))  # [2, 3]
print(CountUp