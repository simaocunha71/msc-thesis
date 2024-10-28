    sum := 0
    for i, value := range lst{
        if i%3 == 0 && i%4 != 0{
            sum += value*value
        }
        if i%4 == 0 && i%3 != 0{
            sum += value*value*value
        }
    }
    return sum
}



