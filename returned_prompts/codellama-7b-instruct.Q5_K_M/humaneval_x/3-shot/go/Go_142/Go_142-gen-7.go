    result := 0
    for i, c := range lst {
        if i%3 == 0 {
            result += int(math.Pow(float64(c), 2))
        } else if i%4 == 0 && i%3 != 0 {
            result += int(math.Pow(float64(c), 3))
        }
    }
    return result
}



