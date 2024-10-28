    n, m := len(a), len(b)

    if n < m {
        return false
    }

    for i := 0; i < m; i++ {
        if !strings.Contains(a, b[i:m+i]) && !strings.Contains(a, b[0:m-i]) {
            return false
        }
    }
    return true
}



