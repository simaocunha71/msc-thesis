    num, err := strconv.ParseFloat(value, 64)
    if err != nil {
        panic(err)
    }
    int_num := int(math.Round(num))
    if num - float64(int_num) > 0.5 {
        int_num++
    }
    return int_num
} 




