    words := strings.Split(sentence, " ")
    result := []string{}
    for _, word := range words {
        if IsPrime(len(word)) {
            result = append(result, word)
        }
    }
    return strings.Join(result, " ")
}

func IsPrime(n int) bool {
    if n <= 1 {
        return false
    }
    for i := 2; i*i <= n; i++ {
        if n%i == 0 {
            return false
        }
    }
    return true
}



