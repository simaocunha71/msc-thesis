    if a <= 1 {
        return false
    }

    primes := []int{2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97}
    factors := make([]int, 0)

    for _, prime := range primes {
        if a%prime == 0 {
            factors = append(factors, prime)
            a /= prime
        }
    }

    if a != 1 {
        return false
    }

    if len(factors) >= 3 {
        for i := 0; i < len(factors)-2; i++ {
            for j := i + 1; j < len(factors)-1; j++ {
                for k := j + 1; k < len(factors); k++ {
                    if factors[i]*factors[j]*factors[k] == a {
                        return true
                    }
                }
            }
        }
    }

    return false
}



