    var result string = strings.ReplaceAll(s,c,"")
    return [2]interface{}{result, IsPalindrome(result)}
}



