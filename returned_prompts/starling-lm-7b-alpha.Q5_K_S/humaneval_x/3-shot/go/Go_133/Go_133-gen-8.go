    result := 0
    for _, i := range lst {
        result += int(math.Ceil(i))*int(math.Ceil(i))
    }
    return result
}



