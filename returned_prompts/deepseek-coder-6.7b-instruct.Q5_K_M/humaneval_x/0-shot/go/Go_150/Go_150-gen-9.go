
    // Check if number is prime
    for i := 2; i < n/2; i++ {
        if n%i == 0 {
            return y
        }
    }

    return x
}

// B:

func isPrime(n int) bool {
    if n <= 1 {
        return false
    }

    for i := 2; i*i <= n; i++ {
        if n%i == 0 {
            return false
        }
    }

    return true
}

func XOrY(n, x, y int) int {
    if isPrime(n) {
        return x
    }

    return y
}

```

## 6.1.2. 

A simple program to find the sum of all prime numbers less than 100.

```go
package main

import "fmt"

func isPrime(n int) bool {
    if n <= 1 {
        return false
    }

    for i := 2; i*i <= n; i++ {
        if n%i == 0 {
            return false
        }
    }

    return true
}

func sumPrimes(n int) int {
    sum := 0
    for i := 2; i < n; i++ {
        if isPrime(i) {
            sum += i
        }
    }

    return sum
}

func main() {
    fmt.Println(sumPrimes(100))
}
```

## 6.1.3. 

A program to check if a number is a palindrome.

```go
package main

import "fmt"

func isPalindrome(n int) bool {
    original := n
    reversed := 0

    for n != 0 {
        remainder := n % 10
        reversed = reversed*10 + remainder
        n = n / 10
    }

    return original == reversed
}

func main() {
    fmt.Println(isPalindrome(121)) //