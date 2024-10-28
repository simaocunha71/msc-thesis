    result := 0
    vowels := []rune{'A', 'E', 'I', 'O', 'U'}
    for i := 0; i < len(s); i += 2{
        if strings.ContainsRune(string(vowels), s[i]){
            result +=1
        }
    }
    return result
}



