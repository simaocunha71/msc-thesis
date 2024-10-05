    if IsPalindrome(str){
        return str
    }
    for i  := len(str); i  > 0; i--  {
        if IsPalindrome(str[0:i]){
            postfix  := str[i:]
            prefix  := str[0:len(str)-len(postfix)]
            result  := str + reverse(postfix)
            return result
         }
     }
    return ""
}

func reverse(str string) string  {
    runes  := []rune(str)
    result  := make([]rune, len(runes))
    for i  := len(runes)  - 1; i  >= 0; i--  {
        result[len(runes)-1-i]  = runes[i]
     }
    return string(result)
}



