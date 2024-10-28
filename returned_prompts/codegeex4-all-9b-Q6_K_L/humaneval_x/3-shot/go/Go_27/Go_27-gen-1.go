    result := make([]rune, 0)
    for _, c := range str {
        if strings.ToLower(string(c)) == string(c){
            result = append(result, rune(strings.ToUpper(string(c))[0]))
        } else {
            result = append(result, rune(strings.ToLower(string(c))[0]))
        }
    }
    return string(result)
}



