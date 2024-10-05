    result := 0
    for _, c := range strconv.Itoa(n){
        if string(c)%2 != 0{
            result += int(string(c)[0] - '0')
        }
    }
    return result
}



