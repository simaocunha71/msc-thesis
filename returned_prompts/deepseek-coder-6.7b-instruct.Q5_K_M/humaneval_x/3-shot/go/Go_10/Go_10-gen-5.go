    if IsPalindrome(str){
        return str
    }else{
        for i  := len(str); i > 0; i--  {
            if IsPalindrome(str[:i]){
                return str + reverse(str[i:])
            }
        }
     }
    return str
}

func reverse(s string) string {
    runes := []rune(s)
    for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
        runes[i], runes[j] = runes[j], runes[i]
    }
    return string(runes)
}



