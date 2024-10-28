    for i  := len(str); i  > 0; i--  {
        if IsPalindrome(str[0:i])  {
            return str[0:i] + Reverse(str[i:]) + Reverse(str[0:i])
         }
     }
     return ""
}

func Reverse(input string) string  {
    runes  := []rune(input)
    result  := make([]rune, 0)
    for i  := len(runes)  - 1; i  >= 0; i--  {
        result  = append(result, runes[i])
     }
    return string(result)
}



