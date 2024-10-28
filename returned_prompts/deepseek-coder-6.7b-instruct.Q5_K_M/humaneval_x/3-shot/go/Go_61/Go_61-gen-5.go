    count := 0
    for _, ch := range brackets {
        if ch == '(' {
            count++
        } else if ch == ')' {
            if count == 0 {
                return false
            }
            count--
        }
    }
    return count == 0
}



