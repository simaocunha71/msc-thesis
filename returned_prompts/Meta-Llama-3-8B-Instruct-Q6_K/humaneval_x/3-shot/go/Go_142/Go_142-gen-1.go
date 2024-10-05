    var sum int
    for i, num := range lst {
        if i%3 == 0 {
            sum += int(math.Pow(float64(num), 2))
        } else if i%4 == 0 && i%3 != 0 {
            sum += int(math.Pow(float64(num), 3))
        } else {
            sum += num
        }
    }
    return sum
} 



