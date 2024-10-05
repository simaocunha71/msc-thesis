    // YOUR CODE GOES HERE
    n, err := strconv.ParseFloat(value, 64)
    if err != nil {
        return 0
    }
    i := int(math.Round(n))
    if math.Abs(float64(i)-n) == 0.5 {
        if i >= 0 {
            i++
        } else {
            i--
        }
    }
    return i
}
