    vowels := "aeiouAEIOU"
    result := strings.Map(func(r rune) rune {
        if strings.Contains(vowels, string(r)) {
            return rune(string(r)[0] + 2)
        }
        if strings.Contains(vowels, strings.ToUpper(string(r))) {
            return rune(strings.ToUpper(string(r))[0] + 2)
        }
        return r
    }, message)
    return strings.Map(func(r rune) rune {
        if strings.Contains("aeiouAEIOU", string(r)) {
            return strings.ToUpper(r)
        }
        return strings.ToLower(r)
    }, result)
}