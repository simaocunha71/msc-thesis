    sum := 0
    for _, num := range lst {
        num = math.Ceil(num)
        sum += int(num*num)
    }
    return sum
}



