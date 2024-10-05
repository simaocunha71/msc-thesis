    primes := [...]int{2,3,5,7,11,13}
    counter := 0
    for _, c := range num {
        n, _ := strconv.Atoi(string(c))
        if n < 10 {
            for _, prime := range primes {
                if n == prime {
                    counter++
                    break
                }
            }
        } else {
            switch c {
            case 'A':
                counter++
            case 'B':
                counter++
            case 'C':
                counter++
            case 'E':
                counter++
            case 'D':
                counter++
            case 'F':
                counter++
            }
        }
    }
    return counter
}



