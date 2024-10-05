    result := make([]string, len(grades))
    for i, gpa := range grades {
        if gpa >= 4.0 {
            result[i] = "A+"
        } else if gpa > 3.7 {
            result[i] = "A"
        } else if gpa > 3.3 {
            result[i] = "A-"
        } else if gpa > 3.0 {
            result[i] = "B+"
        } else if gpa > 2.7 {
            result[i] = "B"
        } else if gpa > 2.3 {
            result[i] = "B-"
        } else if gpa > 2.0 {
            result[i] = "C+"
        } else if gpa > 1.7 {
            result[i] = "C"
        } else if gpa > 1.3 {
            result[i] = "C-"
        } else if gpa > 1.0 {
            result[i] = "D+"
        } else if gpa > 0.7 {
            result[i] = "D"
        } else if gpa > 0.0 {
            result[i] = "D-"
        } else {
            result[i] = "E"
        }
    }
    return result
}