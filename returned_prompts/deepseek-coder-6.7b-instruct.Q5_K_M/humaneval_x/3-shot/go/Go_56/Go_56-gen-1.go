    counter := 0
    for _, c := range brackets {
        if c == '<' {
            counter++
        } else if c == '>' {
            counter--
            if counter < 0 {
                return false
            }
        }
    }
    return counter == 0
}

