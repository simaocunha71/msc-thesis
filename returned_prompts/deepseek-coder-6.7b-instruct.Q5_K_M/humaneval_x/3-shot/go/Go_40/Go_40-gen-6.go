    n := len(l)
    for i  := 0; i < n-2; i++ {
        for j := i+1; j < n-1; j++ {
            for k := j+1; k < n; k++ {
                if l[i] + l[j] + l[k] == 0 {
                    return true
                }
            }
        }
    }
    return false
}



