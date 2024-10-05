    primes := []int{2, 3, 5, 7, 11, 13, 17}
    result := 0
    for _, c := range num {
        if i, _ := strconv.ParseInt(string(c), 16, 64); i != 0 {
            if contains(primes, i) {
                result++
            }
        }
    }
    return result
}

func contains(a []int, b int) bool {
    for _, v := range a {
        if v == b {
            return true
        }
    }
    return false
}



