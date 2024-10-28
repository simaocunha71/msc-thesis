    result := 0
    for _, v := range lst{
        v_rounded := math.Ceil(v)
        result += int(math.Pow(v_rounded, 2))
    }
    return result
}



