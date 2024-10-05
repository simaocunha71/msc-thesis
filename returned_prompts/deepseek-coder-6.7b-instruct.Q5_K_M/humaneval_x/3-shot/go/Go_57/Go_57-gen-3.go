    if len(l) < 2 {
        return true
    }

    increasing := l[len(l)-1] > l[0]

    for i := 0; i < len(l)-1; i++ {
        if (l[i] < l[i+1] && !increasing) || (l[i] > l[i+1] && increasing) {
            return false
        }
    }

    return true
}



