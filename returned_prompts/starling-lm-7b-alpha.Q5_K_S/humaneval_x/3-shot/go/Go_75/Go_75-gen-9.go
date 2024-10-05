    primes := []int{2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97}
    for _, prime := range primes {
        if a%prime != 0 {
            return false
        }
        if prime > math.Sqrt(float64(a)) {
            return true
        }
    }
    return false
}



