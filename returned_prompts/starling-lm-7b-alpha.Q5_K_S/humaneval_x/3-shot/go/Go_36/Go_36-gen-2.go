    result := 0
    for i := 1; i < n; i++ {
        if i % 11 == 0 || i % 13 == 0 {
            if contains(strconv.Itoa(i), '7') {
                result += 1
            }
        }
    }
    return result
}

func contains(s string, c byte) bool {
    for _, v := range s {
        if v == c {
            return true
        }
    }
    return false
}



