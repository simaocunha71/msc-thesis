    result := 0
    for N > 0 {
        result += N % 2
        N /= 2
    }
    return fmt.Sprintf("%b", result)
}



