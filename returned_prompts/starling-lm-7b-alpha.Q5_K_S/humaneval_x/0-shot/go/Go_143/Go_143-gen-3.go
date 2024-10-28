    var words []string
    words = strings.Fields(sentence)

    var ret []string
    for _, word := range words {
        if isPrime(len(word)) {
            ret = append(ret, word)
        }
    }

    return strings.Join(ret, " ")
}

func isPrime(n int) bool {
    if n == 1 {
        return false
    }
    if n == 2 {
        return true
    }
    if n == 3 {
        return true
    }
    if n%2 == 0 {
        return false
    }
    if n%3 == 0 {
        return false
    }

    i := 5
    for i <= int(math.Sqrt(float64(n))) {
        if n%i == 0 {
            return false
        }
        if n%(i + 2) == 0 {
            return false
        }
        i += 6
    }
    return true
}






func WordsInSentence(sentence string) string {
    words := strings.Fields(sentence)
    ret := make([]string, 0)
    for _, word := range words {
        if isPrime(len(word)) {
            ret = append(ret, word)
        }
    }
    return strings.Join(ret, " ")
}

func isPrime(n int) bool {
    if n == 1 {
        return false
    }
    if n == 2 {
        return true
    }
    if n == 3 {
        return true
    }
    if n%2 == 0 {
        return false
    }
    if n%3 == 0 {
        return false
    }

    i := 5
    for i <= int(math.Sqrt(float64(n))) {
        if n%i == 0 {
            return false
        }
        if n%(i+2) == 0 {
            return false
        }
        i += 6
    }
    return true
}


