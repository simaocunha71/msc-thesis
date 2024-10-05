    for i, n := range numbers {
        for _, m := range numbers[i+1:] {
            if math.Abs(n-m) < threshold {
                return true
            }
        }
    }
    return false
}
