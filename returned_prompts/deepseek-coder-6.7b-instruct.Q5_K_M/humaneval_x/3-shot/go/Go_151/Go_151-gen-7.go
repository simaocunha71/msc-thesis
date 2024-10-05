    sum := 0

    for _, num := range lst {
        if num >= 0 && num == float64(int(num)) && int(num)%2 == 1 {
            sum += int(math.Pow(num, 2))
        }
    }

    return sum
}



