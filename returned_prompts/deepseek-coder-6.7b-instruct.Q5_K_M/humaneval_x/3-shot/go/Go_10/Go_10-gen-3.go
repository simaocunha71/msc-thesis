    if IsPalindrome(str){
        return str
    }
    runes  := []rune(str)
    for i  := len(runes); i > 0; i--  {
        if IsPalindrome(string(runes[0:i])){
            prefix  := runes[0:i]
            postfix  := runes[i:len(runes)]
            reverse_prefix  := make([]rune, len(prefix))
            for j  := len(prefix) - 1; j >= 0; j--  {
                reverse_prefix[len(prefix)-1-j]  =  prefix[j]
            }
            return str + string(reverse_prefix)
         }
     }
     return str
}



