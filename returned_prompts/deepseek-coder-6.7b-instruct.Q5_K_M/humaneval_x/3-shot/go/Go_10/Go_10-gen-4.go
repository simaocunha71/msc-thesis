    if IsPalindrome(str) {
        return str
    }
    runes  := []rune(str)
    for i  := len(runes); i > 0; i--  {
        if IsPalindrome(string(runes[0:i])) {
            prefix := runes[0:i]
            suffix := runes[i:]
            reverse := make([]rune, 0)
            for j  := len(suffix) - 1; j >= 0; j--  {
                reverse  := append(reverse, suffix[j])
             }
            return str + string(reverse)
         }
     }
    return str
}

