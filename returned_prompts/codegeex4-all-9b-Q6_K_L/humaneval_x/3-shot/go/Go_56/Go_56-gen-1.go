    open_brackets := 0
    for _, c := range brackets {
        if c == '<' {
            open_brackets += 1
        }else if c== '>'{
            if open_brackets == 0 {
                return false
            }
            open_brackets -= 1
        }
    }
    return open_brackets == 0
}