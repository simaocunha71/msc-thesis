    digitsCount := 0
    hasDot := false
    isValid := true
    for _, v := range file_name {
        if v >= '0' && v <= '9' {
            digitsCount++
        }
        if v == '.' {
            hasDot = true
        }
        if digitsCount > 3 {
            isValid = false
            break
        }
    }

    if digitsCount > 3 || !hasDot {
        isValid = false
    }

    subName := file_name[:strings.IndexByte(file_name, '.')]
    if subName == "" || subName[0] < 'a' || subName[0] > 'z' || subName[0] < 'A' || subName[0] > 'Z' {
        isValid = false
    }

    validAfterDot := file_name[strings.IndexByte(file_name, '.')+1:] == "txt" || file_name[strings.IndexByte(file_name, '.')+1:] == "dll" || file_name[strings.IndexByte(file_name, '.')+1:] == "exe"

    if !validAfterDot {
        isValid = false
    }

    if isValid {
        return "Yes"
    }

    return "No"
}





























































































































































































