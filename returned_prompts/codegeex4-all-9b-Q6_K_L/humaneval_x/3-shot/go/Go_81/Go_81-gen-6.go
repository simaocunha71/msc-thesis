    result := make([]string, len(grades))

    for i := 0; i < len(grades); i++ {
        if grades[i] == 4.0 {
            result[i] = "A+"
        } else if grades[i] > 3.7 {
            result[i] = "A"
        } else if grades[i] > 3.3 {
            result[i] = "A-"
        } else if grades[i] > 3.0 {
            result[i] = "B+"
        } else if grades[i] > 2.7 {
            result[i] = "B"
        } else if grades[i] > 2.3 {
            result[i] = "B-"
        } else if grades[i] > 2.0 {
            result[i] = "C+"
        } else if grades[i] > 1.7 {
            result[i] = "C"
        } else if grades[i] > 1.3 {
            result[i] = "C-"
        } else if grades[i] > 1.0 {
            result[i] = "D+"
        } else if grades[i] > 0.7 {
            result[i] = "D"
        } else if grades[i] > 0.0 {
            result[i] = "D-"
        } else {
            result[i] = "E"
        }
    }

    return result
}



