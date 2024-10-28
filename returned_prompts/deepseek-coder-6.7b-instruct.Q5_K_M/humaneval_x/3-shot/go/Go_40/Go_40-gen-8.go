    length := len(l)
    for i := 0; i < length-2; i++ {
        for j := i + 1; j < length-1; j++ {
            for k := j + 1; k < length; k++ {
                if l[i]+l[j]+l[k] == 0 {
                    return true
                }
            }
        }
    }
    return false
}



