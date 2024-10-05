    max_prime := 0
    for _, num := range lst {
        if num > max_prime {
            is_prime := true
            for i := 2; i * i <= num; i++ {
                if num%i == 0 {
                    is_prime = false
                    break
                }
            }
            if is_prime {
                max_prime = num
            }
        }
    }
    sum_digits := 0
    for _, c := range strconv.Itoa(max_prime) {
        sum_digits += int(c - '0')
    }
    return sum_digits
}