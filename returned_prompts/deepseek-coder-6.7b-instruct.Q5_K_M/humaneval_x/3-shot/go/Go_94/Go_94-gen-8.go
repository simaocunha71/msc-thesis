    var max_prime int = -1
    for  _, num  := range lst  {
        if IsPrime(num) && num > max_prime  {
            max_prime = num
        }
    }
    return SumDigits(max_prime)
}

func IsPrime(n int) bool  {
    if n  != 2 && n % 2 == 0  {
        return false
    }
    for i  := 3; i  * i <= n; i += 2 {
        if n % i == 0  {
            return false
        }
    }
    return n > 1
}

func SumDigits(n int) int  {
    sum  := 0
    for n != 0  {
        sum += n % 10
        n /= 10
    }
    return sum
}

