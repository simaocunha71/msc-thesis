    if n > m {
        return -1
    }
    avg := (n + m) / 2
    if avg%2 == 0 {
        return fmt.Sprintf("0b%d", avg/2)
    }
    return fmt.Sprintf("0b%d1", avg/2)
}



