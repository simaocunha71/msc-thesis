    var result bool

    for i := len(txt) - 1; i >= 0; i-- {
        if rune(txt[i]) >= 65 && rune(txt[i]) <= 90 || rune(txt[i]) >= 97 && rune(txt[i]) <= 122 {
            if i == len(txt)-1 {
                result = true
                break
            } else if txt[i-1] == ' ' {
                result = true
                break
            }
        }
    }
    return result
}






func CheckIfLastCharIsALetter(txt string) bool {
    var result bool
    var lastChar bool
    for i := len(txt) - 1; i >= 0; i-- {
        if rune(txt[i]) >= 65 && rune(txt[i]) <= 90 || rune(txt[i]) >= 97 && rune(txt[i]) <= 122 {
            if i == len(txt) - 1 {
                result = true
                break
            } else if txt[i-1] == ' ' {
                result = true
                break
            }
        }
    }
    return result
}
























func CheckIfLastCharIsALetter(txt string) bool {
    result := false
    for i := len(txt) - 1; i >= 0; i-- {
        if (rune(txt[i]) >= 65 && rune(txt[i]) <= 90) || (rune(txt[i]) >= 97 && rune(txt[i]) <= 122) {
            if i == len(txt)-1 {
                result = true
                break
            } else if txt[i-1] == ' ' {
                result = true
                break
            }
        }
    }
    return result
}




















