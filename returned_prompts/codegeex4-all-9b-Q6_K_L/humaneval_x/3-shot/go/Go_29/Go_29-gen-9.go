    result := make([]string, 0)
    for _, s := range strings{
        if strings.HasPrefix(s, prefix){
            result = append(result, s)
        }
    }
    return result
}



