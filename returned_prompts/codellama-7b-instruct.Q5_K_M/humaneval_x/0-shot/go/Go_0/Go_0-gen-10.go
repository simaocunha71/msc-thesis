    for i, x := range numbers {
        for j, y := range numbers {
            if i == j {
                continue
            }
            if math.Abs(x-y) < threshold {
                return true
            }
        }
    }
    return false
}
