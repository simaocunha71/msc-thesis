    count := 0
    for _, c := range brackets {
        if c == '<' {
            count++
        } else if c == '>' {
            count--
            if count < 0 {
                return false
            }
        }
    }
    return count == 0
}



