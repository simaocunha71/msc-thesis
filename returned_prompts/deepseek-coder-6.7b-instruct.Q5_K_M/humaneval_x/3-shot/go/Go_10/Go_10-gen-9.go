    if IsPalindrome(str)  {
        return str
    }
    for i  := len(str) ; i  > 0; i--  {
        if IsPalindrome(str[0:i])  {
            prefix  := str[0:i]
            postfix  := str[i:len(str)]
            result  := str + Reverse(prefix)
            return result
         }
     }
     return ""
 }

 func Reverse(s string) string  {
     runes  := []rune(s)
     for i, j  := 0, len(runes)  - 1; i < j; i, j  = i+1, j-1  {
         runes[i], runes[j]  = runes[j], runes[i]
     }
     return string(runes)
 }



