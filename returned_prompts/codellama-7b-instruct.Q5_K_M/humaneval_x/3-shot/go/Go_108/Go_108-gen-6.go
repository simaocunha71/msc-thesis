    count := 0

    for _, num := range arr{
        sum := 0
        for _, digit := range strconv.Itoa(num){
            sum += int(digit - '0')
        }
        if sum > 0{
            count += 1
        }
    }
    return count
}



