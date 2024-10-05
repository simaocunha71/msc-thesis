    result := 0
    for _, number := range arr{
        sum := 0
        for _, digit := range strconv.Itoa(number){
            sum += int(digit) - 48
        }
        if sum > 0{
            result += 1
        }
    }
    return result
}



