    var num_int float64
    var err error
    if strings.Contains(value, "."){
        num_int, err = strconv.ParseFloat(value, 64)
        if err != nil{
            return 0
        }
    }else{
        num_int, err = strconv.ParseInt(value, 10, 64)
        if err != nil{
            return 0
        }
    }
    num_int = math.Floor(num_int + .5)
    return int(num_int)
}



