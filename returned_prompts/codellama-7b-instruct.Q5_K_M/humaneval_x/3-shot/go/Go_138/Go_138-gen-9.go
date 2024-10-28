    for i := 0; i < n; i += 2 {
        for j := i + 1; j < n; j += 2 {
            for k := j + 1; k < n; k += 2 {
                if (i + j + k) == n {
                    return true
                }
            }
        }
    }
    return false
}



