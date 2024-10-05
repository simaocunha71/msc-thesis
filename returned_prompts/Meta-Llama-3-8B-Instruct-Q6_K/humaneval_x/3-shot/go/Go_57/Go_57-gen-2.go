    for i := 1; i < len(l); i++ {
        if l[i] > l[i-1] {
            for j := i; j > 0; j-- {
                if l[j] > l[j-1] {
                    return true
                }else if l[j] < l[j-1] {
                    return false
                }
            }
        }else if l[i] < l[i-1] {
            for j := i; j > 0; j-- {
                if l[j] < l[j-1] {
                    return true
                }else if l[j] > l[j-1] {
                    return false
                }
            }
        }
    }
    return true
}