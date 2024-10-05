    if len(l) < 2 {
        return true
    }
    increasing := l[len(l)-1] > l[0]
    for i := 0; i < len(l)-1; i++ {
        if (l[i+1] > l[i] && !increasing) || (l[i+1] < l[i] && increasing) {
            return false
        }
    }
    return true
}



