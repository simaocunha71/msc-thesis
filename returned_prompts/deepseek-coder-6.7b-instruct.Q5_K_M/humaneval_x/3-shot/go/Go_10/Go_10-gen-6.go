    for i := len(str); i  != 0; i--  {
        if IsPalindrome(str[0:i])  {
            postfix  := str[i:]
            return str + Reverse(postfix)
        }
     }
    return str
}



