    var letterGrade string
    result := make([]string, len(grades))

    for i, grade := range grades {
        switch {
        case grade == 4.0:
            letterGrade = "A+"
        case grade > 3.7:
            letterGrade = "A"
        case grade > 3.3:
            letterGrade = "A-"
        case grade > 3.0:
            letterGrade = "B+"
        case grade > 2.7:
            letterGrade = "B"
        case grade > 2.3:
            letterGrade = "B-"
        case grade > 2.0:
            letterGrade = "C+"
        case grade > 1.7:
            letterGrade = "C"
        case grade > 1.3:
            letterGrade = "C-"
        case grade > 1.0:
            letterGrade = "D+"
        case grade > 0.7:
            letterGrade = "D"
        case grade > 0.0:
            letterGrade = "D-"
        default:
            letterGrade = "E"
        }
        result[i] = letterGrade
    }
    return result
}



