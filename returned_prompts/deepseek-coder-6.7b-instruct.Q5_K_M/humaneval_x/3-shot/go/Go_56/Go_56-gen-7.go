    count := 0
    for _, bracket := range brackets {
        if bracket == '<' {
            count++
        } else if bracket == '>' {
            count--
            if count < 0 {
                return false
            }
        }
    }
    return count == 0
}


