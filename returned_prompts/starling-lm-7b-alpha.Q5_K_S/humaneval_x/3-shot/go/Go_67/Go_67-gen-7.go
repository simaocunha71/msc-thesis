    var result int
    var index int
    for index = 0;index<len(s);index++ {
        if s[index] == 'a' {
            break
        }
    }
    for index++;index<len(s);index++ {
        if s[index] == 'p' {
            break
        }
    }
    result = n - (strings.Count(s[index+1:],'a') + strings.Count(s[index+1:],'o'))
    return result
}



