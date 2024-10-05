    var sum int
    for i, n := range lst {
        if (i+1)%3 == 0 {
            sum += int(math.Pow(float64(n), 2))
        } else if (i+1)%4 == 0 && (i+1)%3 != 0 {
            sum += int(math.Pow(float64(n), 3))
        } else {
            sum += n
        }
    }
    return sum
}