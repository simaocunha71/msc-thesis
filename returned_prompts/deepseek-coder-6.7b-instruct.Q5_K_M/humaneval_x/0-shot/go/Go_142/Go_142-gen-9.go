    sum := 0
    for i := range lst {
        if i%3 == 0 {
            sum += int(math.Pow(float64(lst[i]), 2))
        } else if i%4 == 0 {
            sum += int(math.Pow(float64(lst[i]), 3))
        } else {
            sum += lst[i]
        }
    }
    return sum
}

