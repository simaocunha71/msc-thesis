    result := strings[0]
    for _, str := range strings {
        if len(str) > len(result) {
            result = str
        }
    }
    return result
}



