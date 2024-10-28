    var result string
    for i := 0; i < len(s); i++ {
        if !strings.Contains(c, string(s[i])) {
            result += string(s[i])
        }
    }
    var is_palindrome bool
    if strings.EqualFold(result, strings.Reverse(result)) {
        is_palindrome = true
    } else {
        is_palindrome = false
    }
    return [2]interface{}{result, is_palindrome}
}  //end of function
}  //end of package


