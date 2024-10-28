    count := 0
    for _, num := range arr{
        sum := 0
        if num < 0{
            num *= -1
        }
        for num != 0{
            sum += num % 10
            num /= 10
        }
        if sum > 0{
            count += 1
        }
    }
    return count
}

