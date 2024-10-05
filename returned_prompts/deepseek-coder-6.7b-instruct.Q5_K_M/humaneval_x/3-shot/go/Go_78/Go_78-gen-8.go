    primeCount := 0
    primeArray := []string{"2", "3", "5", "7", "B", "D"}
    for _, c := range num {
        if contains(primeArray, string(c)) {
            primeCount++
        }
    }
    return primeCount
}

func contains(s []string, str string) bool {
    for _, v := range s {
        if v == str {
            return true
        }
    }
    return false
}



