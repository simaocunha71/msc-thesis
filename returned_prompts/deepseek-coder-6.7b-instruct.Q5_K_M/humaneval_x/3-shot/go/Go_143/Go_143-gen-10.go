    words := strings.Fields(sentence)
    res := []string{}

    isPrime := func(n int) bool {
        if n < 2 {
            return false
        }
        for i := 2; i*i <= n; i++ {
            if n%i == 0 {
                return false
            }
        }
        return true
    }

    for _, word := range words {
        if isPrime(len(word)) {
            res = append(res, word)
        }
    }
    return strings.Join(res, " ")
}



