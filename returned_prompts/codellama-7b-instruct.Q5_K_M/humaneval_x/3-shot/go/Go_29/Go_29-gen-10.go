    result := make([]string,0)

    for _, str := range strings{
        if len(str) > 0 && str[0] == prefix[0]{
            result = append(result, str)
        }
    }
    return result
}



