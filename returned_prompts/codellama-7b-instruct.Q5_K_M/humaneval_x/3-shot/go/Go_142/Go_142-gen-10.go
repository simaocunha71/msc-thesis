    result := 0
    for index, value := range lst{
        if index%3 == 0{
            result += value*value
        }else if index%4 == 0{
            result += value*value*value
        }
    }
    return result
}



