    result := ""
    isPalindrome := true
    for _,v := range s {
        if !strings.Contains(c,string(v)){
            result += string(v)
        }else {
            isPalindrome = false
        }
    }
    return [2]interface{}{result,isPalindrome}
}



