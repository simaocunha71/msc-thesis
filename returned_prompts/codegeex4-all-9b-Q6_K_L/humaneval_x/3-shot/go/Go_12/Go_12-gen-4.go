    if len(strings) == 0{
        return nil
    }
    result := strings[0]
    for _, s := range strings {
        if len(s) > len(result){
            result = s
        }
    }
    return result
}



