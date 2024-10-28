    result := make([]rune, 0)
    for _, c := range message {
        if !(c >= 'a' && c <= 'z') && !(c >= 'A' && c <= 'Z'){
            result = append(result, c)
        }else{
            if c >= 'a' && c <= 'z'{
                result = append(result, c+2)
            }else{
                result = append(result, c-2)
            }
        }
    }
    return string(result)
}



