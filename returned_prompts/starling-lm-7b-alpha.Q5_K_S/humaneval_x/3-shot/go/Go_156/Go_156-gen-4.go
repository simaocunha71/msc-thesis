    if number < 1 || number > 1000 {
        panic("Invalid number")
    }
    result := make([]rune, 0)
    thousands := number / 1000
    for i := 0; i < thousands; i++ {
        result = append(result, 'm')
    }
    hundreds := (number % 1000) / 100
    for i := 0; i < hundreds; i++ {
        result = append(result, 'c')
    }
    if hundreds > 0 {
        result = append(result, '.')
    }
    tens := (number % 100) / 10
    for i := 0; i < tens; i++ {
        result = append(result, 'x')
    }
    units := number % 10
    for i := 0; i < units; i++ {
        result = append(result, 'i')
    }
    return string(result)
}



