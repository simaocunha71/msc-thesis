    if n < 2 {
        return []int{}
    }
    result := make([]int, 0)
    result = append(result, 2)

    for i := 3; i < n; i += 2 {
        if isPrime(i) {
            result = append(result, i)
        }
    }
    return result
}

func isPrime(number int) bool {
    if number == 2 {
        return true
    }

    for i := 2; i < number; i++ {
        if number % i == 0 {
            return false
        }
    }
    return true
}



