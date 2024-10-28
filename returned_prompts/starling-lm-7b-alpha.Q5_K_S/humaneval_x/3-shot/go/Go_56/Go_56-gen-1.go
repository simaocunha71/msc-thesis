    result := 0
    for _, c := range brackets {
        if c == '<' {
            result++
        }else if c=='>'{
            result--
        }
        if result < 0 {
            return false
        }
    }
    return result==0
}



