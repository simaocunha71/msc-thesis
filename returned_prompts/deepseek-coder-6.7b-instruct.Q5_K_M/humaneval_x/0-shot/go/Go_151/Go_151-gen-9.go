    sum := 0.0
    for _, v := range lst {
        if v > 0 && v == math.Floor(v) && int(v) % 2 != 0 {
            sum += math.Pow(v, 2)
        }
    }
    return int(sum)
}

