    var result string
    for _, word := range strings.Fields(sentence) {
        if IsPrime(len(word)) {
            result += word + " "
        }
    }
    return strings.TrimSpace(result)
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




