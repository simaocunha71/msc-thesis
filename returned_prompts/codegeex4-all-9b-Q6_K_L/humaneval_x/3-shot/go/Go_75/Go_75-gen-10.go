    primes := []int{2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97}

    for _, p1 := range primes {
        for _, p2 := range primes {
            for _, p3 := range primes {
                if p1 * p2 * p3 == a {
                    return true
                }
            }
        }
    }
    return false
}



