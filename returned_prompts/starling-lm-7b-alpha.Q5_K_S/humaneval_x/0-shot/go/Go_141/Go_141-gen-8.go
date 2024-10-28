    const validExtensions = []string{"txt", "exe", "dll"}
    const maxDigits = 3
    var countDigits int
    var nameBeforeDot string
    var nameAfterDot string
    var isValid bool
    for _, v := range file_name {
        if v >= '0' && v <= '9' {
            countDigits++
        } else if v == '.' {
            if len(nameBeforeDot) == 0 || nameBeforeDot[0] < 'a' || nameBeforeDot[0] > 'z' || nameBeforeDot[0] < 'A' || nameBeforeDot[0] > 'Z' {
                isValid = false
            }
            nameBeforeDot = ""
            nameAfterDot = file_name[len(nameBeforeDot)+1:]
        } else {
            nameBeforeDot += string(v)
        }
    }
    if countDigits > maxDigits || len(nameAfterDot) == 0 {
        isValid = false
    }
    for _, v := range validExtensions {
        if nameAfterDot == v {
            isValid = true
            break
        }
    }
    return strings.Join([]string{"Yes", "No"}, isValid && len(nameAfterDot) > 0)
}
















































































































































































































