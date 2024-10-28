    for i := 0; i < len(l)-1; i++ {
        if (l[i] < l[i+1]) {
            for j := i+1; j < len(l); j++ {
                if l[j] < l[j-1] {
                    return false
                }
            }
            return true
        } else if (l[i] > l[i+1]) {
            for j := i+1; j < len(l); j++ {
                if l[j] > l[j-1] {
                    return false
                }
            }
            return true
        }
    }
    return true
}