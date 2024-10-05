    result := make([]rune, 0)
    for _, c := range message {
        if c >= 'a' && c <= 'z' {
            if "aeiou".Index(string(c)) != -1 {
                result = append(result, 'a'+(c-'a'+2)%26)
            }else {
                result = append(result, 'a'+(c-'a'-2+26)%26)
            }
        }else {
            result = append(result, c)
        }
    }
    return string(result)
}



