    result := 0
    for _,v := range arr{
        sum := 0
        for _,v2 := range strconv.Itoa(v){
            sum += v2 - '0'
        }
        if sum > 0{
            result += 1
        }
    }
    return result
}



