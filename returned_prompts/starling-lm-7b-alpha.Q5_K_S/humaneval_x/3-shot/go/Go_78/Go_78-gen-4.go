    primes := []string{"2","3","5","7","B","D"}
    result := 0
    for _, c := range num {
        switch {
        case c >= '0' && c <= '9':
            n := int(c - '0')
            if contains(primes,string(n)) {
                result += 1
            }
        case c >= 'A' && c <= 'F':
            n := string(c) + "0123456789"
            if contains(primes,n) {
                result += 1
            }
        }
    }
    return result
}

func contains(slice []string, elem string) bool {
    for _, e := range slice {
        if e == elem {
            return true
        }
    }
    return false
}



