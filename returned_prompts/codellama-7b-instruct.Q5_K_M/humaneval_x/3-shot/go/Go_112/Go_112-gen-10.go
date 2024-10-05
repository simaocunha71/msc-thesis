    result_string := strings.Replace(s,c,"",-1)
    return [2]interface{}{result_string,IsPalindrome(result_string)}
}



