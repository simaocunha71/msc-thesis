
    if n <= 1 {
        return false
    }

B:

    if n == 2 || n == 3 {
        return true
    }

C:

    if n%2 == 0 || n%3 == 0 {
        return false
    }

D:

    i := 5
    w := 2

    for i*i <= n {
        if n%i == 0 {
            return false
        }

        i += w
        w = 6 - w
    }

E:

    return true
}

// To test the function, you can use a main function as below:

func main()  {

F:

    fmt.Println(IsPrime(13441))
    fmt.Println(IsPrime(61))
    fmt.Println(IsPrime(4))
    fmt.Println(IsPrime(1))
    fmt.Println(IsPrime(101))
    fmt.Println(IsPrime(6))
    fmt.Println(IsPrime(11))

G:

}
```


## Explanation

This program defines a function called `IsPrime` that checks if a given number `n` is prime. A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.

The function starts by checking if `n` is less than or equal to 1. If it is, the function immediately returns `false`, because the numbers less than 2 are not prime.

Next, the function checks if `n` is 2 or 3. If it is, the function returns `true`, because 2 and 3 are prime numbers.

Then, the function checks if `n` is divisible by 2 or 3. If it is, the function returns `false`, because `n` is not a prime number.

After that, the function starts a loop that checks all possible factors of `n`. The loop starts from 5 and increments `i` by `w` each iteration, and alternates between 2 and 4 for `w`. This is done because all primes