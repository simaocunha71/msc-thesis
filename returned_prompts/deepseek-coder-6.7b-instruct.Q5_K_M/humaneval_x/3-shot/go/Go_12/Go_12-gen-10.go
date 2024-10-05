    if len(strings) == 0{
        return nil
    }

    max_len := 0
    max_str := ""

    for _, str := range strings{
        if len(str) > max_len{
            max_len = len(str)
            max_str = str
        }
    }

    return max_str
}



