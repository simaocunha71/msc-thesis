    count := 0
    for _, b := range brackets {
        if b == '(' {
            count++
        } else if b == ')' {
            if count == 0 {
                return false
            }
            count--
        }
    }
    return count == 0
}



