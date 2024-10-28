    result := 0
    for index, value := range lst{
        if index%3 == 0{
            result += int(math.Pow(float64(value), 2))
        }else if index%4 == 0 && index%3 != 0{
            result += int(math.Pow(float64(value), 3))
        }
    }
    return result
}



