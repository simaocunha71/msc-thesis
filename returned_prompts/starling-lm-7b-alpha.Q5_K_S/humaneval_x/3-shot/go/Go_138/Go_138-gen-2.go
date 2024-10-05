    for i := 1; i <= n/2; i++ {
        if (n - i*2) % 2 == 0 {
            return true
        }
    }
    return false
}



