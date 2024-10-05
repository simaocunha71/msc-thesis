    if len(b) > len(a) {
        return false
    }

    for i := 0; i <= len(a) - len(b); i++ {
        if strings.Contains(a[i:i+len(b)], b) {
            return true
        }
    }
    return false
}



