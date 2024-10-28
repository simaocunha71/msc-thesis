    result := make([]string, 0)

    for _, s := range stringList{
        if strings.Contains(s, substring){
            result = append(result, s)
        }
    }
    return result
}



