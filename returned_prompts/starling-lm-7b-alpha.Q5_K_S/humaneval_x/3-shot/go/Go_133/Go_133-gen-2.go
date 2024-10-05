    result := int(0)
    for _, i := range lst {
        i_int := int(math.Ceil(i))
        result += i_int*i_int
    }
    return result
}



