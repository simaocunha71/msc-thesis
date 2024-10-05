    result := 0
    for _, num := range arr{
        if strconv.Itoa(num)[0] == "-"{
            continue
        }
        sum := 0
        for _, digit := range strconv.Itoa(num){
            sum += int(digit - '0')
        }
        if sum > 0{
            result++
        }
    }
    return result
}



