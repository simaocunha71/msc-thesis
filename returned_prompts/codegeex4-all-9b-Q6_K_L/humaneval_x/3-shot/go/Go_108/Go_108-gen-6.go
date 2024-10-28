    result := 0

    for _, num := range arr{
        digits := strconv.Itoa(num)
        sum := 0
        for _, digit := range digits{
            num, _ := strconv.Atoi(string(digit))
            sum += num
        }

        if sum > 0{
            result += 1
        }
    }

    return result
}

