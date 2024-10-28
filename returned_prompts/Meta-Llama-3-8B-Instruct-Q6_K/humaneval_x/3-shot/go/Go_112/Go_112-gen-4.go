    var result string
    var is_palindrome bool

    for _, c := range s {
        if !strings.Contains(c, string(c)) {
            result += string(c)
        }
    }

    if strings.EqualFold(result, strings.Reverse(result)) {
        is_palindrome = true
    } else {
        is_palindrome = false
    }

    return [2]interface{}{result, is_palindrome}
}
// 
// 
// 
// 
// 





