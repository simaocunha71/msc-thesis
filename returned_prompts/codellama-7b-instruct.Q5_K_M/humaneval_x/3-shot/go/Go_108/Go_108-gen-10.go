    result := 0
    for _, v := range arr{
        s := strconv.Itoa(v)
        var sum int
        for _, c := range s{
            sum += int(c - '0')
        }
        if sum > 0{
            result += 1
        }
    }
    return result
}



