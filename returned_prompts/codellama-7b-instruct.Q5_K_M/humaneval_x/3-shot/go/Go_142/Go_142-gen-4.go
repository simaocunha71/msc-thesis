    result := 0
    for i, n := range lst {
        if i%3 == 0 {
            result += int(math.Pow(float64(n), 2))
        } else if i%4 == 0 && i%3 != 0 {
            result += int(math.Pow(float64(n), 3))
        }
    }
    return result
}



