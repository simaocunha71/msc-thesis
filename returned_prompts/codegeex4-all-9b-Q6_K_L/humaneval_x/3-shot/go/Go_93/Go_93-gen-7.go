    vowels := "aeiouAEIOU"
    result := make([]rune, 0)
    for _, c := range message {
        if strings.ContainsRune(vowels, c){
            if c >= 'a' && c <= 'z'{
                c += 2
            }else{
                c += 2
            }
        }else{
            if c >= 'a' && c <= 'z'{
                c -= 32
            }else{
                c += 32
            }
        }
        result = append(result,c)
    }
    return string(result)
}

