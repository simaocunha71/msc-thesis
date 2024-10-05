    for i, _ := range l {
        for j := i + 1; j < len(l); j++ {
            if l[i] + l[j] == 0 {
                return true
            }
        }
    }
    return false
}



