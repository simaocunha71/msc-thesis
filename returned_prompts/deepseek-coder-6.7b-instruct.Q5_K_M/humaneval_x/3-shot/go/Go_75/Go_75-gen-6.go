    primeProduct := 1
    counter := 0
    for i := 2; a != 1; i++ {
        for a % i == 0 {
            if primeProduct == 1 || primeProduct == i {
                primeProduct *= i
                counter++
            } else {
                return false
            }
            a /= i
        }
    }
    return primeProduct != 1 && counter == 3
}



