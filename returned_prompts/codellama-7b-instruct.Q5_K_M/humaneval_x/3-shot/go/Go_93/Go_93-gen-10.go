    var result []rune = make([]rune, 0)

    for _, c := range message {
        if strings.Contains("aeiouAEIOU", string(c)) {
            result = append(result, rune(int(c) + 2))
        }else{
            result = append(result, rune(int(c) - 32))
        }
    }

    return string(result)
}



