    var result string =""
    for _,v:=range s{
        if !strings.Contains(c,string(v)){
            result+=string(v)
        }
    }
    return [2]interface{}{result,isPalindrome(result)}
}

func isPalindrome(s string) bool {
    for i := 0; i < len(s)/2; i++ {
        if s[i] != s[len(s)-i-1] {
            return false
        }
    }
    return true
}



