    max_prime := math.MaxInt32
    for _, v := range lst {
        if v > max_prime {
            max_prime = v
        }
    }
    // Check if number is prime
    for i := 2; i < int(math.Sqrt(float64(max_prime))); i++ {
        if max_prime % i == 0 {
            max_prime = math.MaxInt32
            break
        }
    }
    if max_prime == math.MaxInt32 {
        return 0
    }
    str_max_prime := strconv.Itoa(max_prime)
    result := 0
    for _, c := range str_max_prime {
        result += int(c - '0')
    }
    return result
}



