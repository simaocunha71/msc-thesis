    result := make([]rune, 0)

    for _, c := range text {
        if c==' ' {
            result = append(result, '_')
        }else{
            result = append(result, c)
        }
    }
    return string(result)
}



