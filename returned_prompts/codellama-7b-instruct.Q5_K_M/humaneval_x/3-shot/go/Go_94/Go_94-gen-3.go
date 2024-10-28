    var largest_prime int
    var sum int

    for i := 0; i < len(lst); i++ {
        if isPrime(lst[i]){
            if lst[i] > largest_prime {
                largest_prime = lst[i]
            }
        }
    }
    for j := 0; j < len(strconv.Itoa(largest_prime)); j++ {
        sum += int(strconv.Itoa(largest_prime)[j]-'0')
    }
    return sum
}

func isPrime(n int) bool {
    if n < 2 {
        return false
    }
    for i := 2; i * i <= n; i++ {
        if n % i == 0 {
            return false
        }
    }
    return true
}



