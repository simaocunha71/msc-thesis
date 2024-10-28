    len_l := len(l)
    if len_l < 3 {
        return false
    }
    for i := 0; i < len_l - 2; i++ {
        for j := i+1; j < len_l - 1; j++ {
            for k := j + 1; k < len_l; k++ {
                if l[i] + l[j] + l[k] == 0 {
                    return true
                }
            }
        }
    }
    return false
}



