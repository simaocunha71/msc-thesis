    prime_numbers := []int{2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97}

    for _, p := range prime_numbers {
        if p > a {
            break
        }
        if a % p == 0 {
            a = a / p
        }
    }

    return a == 1
}



