    result := 0
    for _, num := range arr {
        s := strconv.Itoa(num)
        sum := 0
        for _, digit := range s{
            sum += int(digit - '0')
        }
        if sum > 0 {
            result += 1
        }
    }
    return result
}



