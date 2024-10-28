    max_prime := 0

    for _, num := range lst {
        if num > max_prime && IsPrime(num) {
            max_prime = num
        }
    }

    return SumDigits(max_prime)
}

func SumDigits(num int) int {
    result := 0

    for num > 0 {
        result += num % 10
        num /= 10
    }

    return result
}

func IsPrime(num int) bool {
    if num <= 1 {
        return false
    }

    for i := 2; i <= int(math.Sqrt(float64(num))); i++ {
        if num%i == 0 {
            return false
        }
    }

    return true
}



