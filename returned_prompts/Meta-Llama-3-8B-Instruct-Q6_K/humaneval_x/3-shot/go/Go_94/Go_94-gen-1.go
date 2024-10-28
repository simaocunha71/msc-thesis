    var max_prime int
    for _, num := range lst {
        if is_prime(num) {
            if max_prime < num {
                max_prime = num
            }
        }
    }

    sum := 0
    for _, digit := range strconv.Itoa(max_prime) {
        sum += int(digit - '0')
    }

    return sum
}

func is_prime(n int) bool {
    if n < 2 {
        return false
    }
    for i := 2; i <= int(math.Sqrt(float64(n))); i++ {
        if n%i == 0 {
            return false
        }
    }
    return true
}