    if len(dict) == 0{
        return false
    }

    caseCheck := -1 // -1 for no check, 0 for lower case, 1 for upper case

    for key, _ := range dict {
        switch key.(type) {
        case string:
            str := key.(string)
            if caseCheck == -1 {
                if strings.ToLower(str) == str {
                    caseCheck = 0
                } else if strings.ToUpper(str) == str {
                    caseCheck = 1
                } else {
                    return false
                }
            } else if (caseCheck == 0 && strings.ToLower(str) != str) || (caseCheck == 1 && strings.ToUpper(str) != str) {
                return false
            }
        default:
            return false
        }
    }
    return true
}



