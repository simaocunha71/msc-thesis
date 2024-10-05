    if len(s0) != len(s1){
        return false
    }

    chars := make([]int, 256)
    for _, c := range s0{
        chars[c] += 1
    }

    for _, c := range s1{
        chars[c] -= 1
        if chars[c] < 0{
            return false
        }
    }

    return true
}



