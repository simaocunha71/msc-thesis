    if IsPalindrome(str)  {
        return str
    }

    runes  := []rune(str)
    for i := len(runes); i > 0; i--  {
        if IsPalindrome(string(runes[0:i]))  {
            suffix  := runes[i:]
            prefix  := runes[0:i]
            result  := make([]rune, 0)
            result  = append(result, prefix...)
            for j  := len(suffix)  - 1; j >= 0; j--  {
                result  = append(result, suffix[j])
             }
            return string(result)
        }
    }
    return str
}



