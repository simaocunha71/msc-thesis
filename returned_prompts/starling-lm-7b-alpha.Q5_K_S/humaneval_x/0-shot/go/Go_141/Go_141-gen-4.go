    var result = "No"
    var count = 0
    for _, char := range file_name {
        if char >= '0' && char <= '9' {
            count++
        }
        if count > 3 {
            break
        }
    }
    if count <= 3 {
        result = "Yes"
    }
    dotIndex := strings.Index(file_name, ".")
    if dotIndex != -1 {
        beforeDot := file_name[:dotIndex]
        afterDot := file_name[dotIndex+1:]
        if len(beforeDot) == 0 {
            result = "No"
        } else {
            if !strings.HasPrefix(beforeDot, "A") && !strings.HasPrefix(beforeDot, "B") && !strings.HasPrefix(beforeDot, "C") && !strings.HasPrefix(beforeDot, "D") && !strings.HasPrefix(beforeDot, "E") && !strings.HasPrefix(beforeDot, "F") && !strings.HasPrefix(beforeDot, "G") && !strings.HasPrefix(beforeDot, "H") && !strings.HasPrefix(beforeDot, "I") && !strings.HasPrefix(beforeDot, "J") && !strings.HasPrefix(beforeDot, "K") && !strings.HasPrefix(beforeDot, "L") && !strings.HasPrefix(beforeDot, "M") && !strings.HasPrefix(beforeDot, "N") && !strings.HasPrefix(beforeDot, "O") && !strings.HasPrefix(beforeDot, "P") && !strings.HasPrefix(beforeDot, "Q") && !strings.HasPrefix(beforeDot, "R") && !strings.HasPrefix(beforeDot, "S") && !strings.HasPrefix(beforeDot, "T") && !strings.HasPrefix(beforeDot, "U") && !strings.HasPrefix(beforeDot, "V") && !strings.HasPrefix(beforeDot, "W") && !strings.HasPrefix(beforeDot, "X") && !strings.HasPrefix(beforeDot, "Y") && !strings.HasPrefix(beforeDot, "Z") {
            result = "No"
        } else {
           