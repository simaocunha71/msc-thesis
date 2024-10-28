    var largestPrime, sum int
    largestPrime = -1

    for _, num := range lst {
        if IsPrime(num) && num > largestPrime {
            largestPrime = num
        }
    }

    if largestPrime != -1 {
        sum = 0
        for _, digit := range strconv.Itoa(largestPrime) {
            num, _ := strconv.Atoi(string(digit))
            sum += num
        }
    }

    return sum
}

func IsPrime(n int) bool {
    if n <= 1 {
        return false
    }
    if n <= 3 {
        return true
    }

    if n%2 == 0 || n%3 == 0 {
        return false
    }

    i := 5
    for i*i <= n {
        if n%i == 0 || n%(i+2) == 0 {
            return false
        }
        i += 6
    }

    return true
}



