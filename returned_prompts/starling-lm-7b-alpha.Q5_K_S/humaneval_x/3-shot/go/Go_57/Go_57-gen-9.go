    for i := 0; i < len(l)-1; i++ {
        if l[i+1] - l[i] > 0 {
            return false
        }
    }
    return true
}



