    result  := make([]string, len(grades))

    for i, gpa := range grades {
        switch {
        case gpa == 4.0:
            result[i] = "A+"
        case gpa > 3.7:
            result[i] = "A"
        case gpa > 3.3:
            result[i] = "A-"
        case gpa > 3.0:
            result[i] = "B+"
        case gpa > 2.7:
            result[i] = "B"
        case gpa > 2.3:
            result[i] = "B-"
        case gpa > 2.0:
            result[i] = "C+"
        case gpa > 1.7:
            result[i] = "C"
        case gpa > 1.3:
            result[i] = "C-"
        case gpa > 1.0:
            result[i] = "D+"
        case gpa > 0.7:
            result[i] = "D"
        case gpa > 0.0:
            result[i] = "D-"
        default:
            result[i] = "E"
        }
    }

    return result
}



