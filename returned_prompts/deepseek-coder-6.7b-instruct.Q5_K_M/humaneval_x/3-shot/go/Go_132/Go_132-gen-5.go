    count := 0
    for i := 0; i < len(s); i++ {
        if s[i] == '[' {
            count++
        } else {
            if count == 0 {
                return false
            }
            count--
        }
    }
    return count != 0
}



