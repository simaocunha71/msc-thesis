    result := make([]string,0)
    for _, word := range strings.Split(sentence," "){
        if is_prime(len(word)){
            result = append(result,word)
        }
    }
    return strings.Join(result," ")
}

func is_prime(n int) bool {
    for i := 2; i*i <= n; i++ {
        if n%i == 0 {
            return false
        }
    }
    return true
}



