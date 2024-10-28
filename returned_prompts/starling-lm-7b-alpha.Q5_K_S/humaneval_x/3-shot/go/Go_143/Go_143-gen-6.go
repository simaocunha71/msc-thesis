    var words []string
    words = strings.Split(sentence, " ")
    var result []string
    for _, word := range words {
        if is_prime(len(word)) {
            result = append(result, word)
        }
    }
    return strings.Join(result, " ")
}

func is_prime(num int) bool {
    if num == 1 {
        return false
    }
    for i := 2; i * i <= num; i++ {
        if num % i == 0 {
            return false
        }
    }
    return true
}



