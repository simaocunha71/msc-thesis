    largestPrime := 2

    for n % 2 == 0{
        n = n / 2
    }

    for i := 3; i * i <= n; i = i + 2{
        while n % i == 0{
            largestPrime = i
            n = n / i
        }
    }

    if n > 2{
        largestPrime = n
    }

    return largestPrime
}



