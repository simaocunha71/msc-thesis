    for _, c := range b {
        if a.Index(string(c)) > -1 {
            return true
        }
    }
    return b == string(a[1:] + a[:1])
}



