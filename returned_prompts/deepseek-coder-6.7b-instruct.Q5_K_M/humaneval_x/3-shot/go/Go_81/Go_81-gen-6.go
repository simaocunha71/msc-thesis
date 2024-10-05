    letterGrades  := make([]string, len(grades))

    for i, grade := range grades {
        switch {
        case grade == 4.0:
            letterGrades[i] = "A+"
        case grade > 3.7:
            letterGrades[i] = "A"
        case grade > 3.3:
            letterGrades[i] = "A-"
        case grade > 3.0:
            letterGrades[i] = "B+"
        case grade > 2.7:
            letterGrades[i] = "B"
        case grade > 2.3:
            letterGrades[i] = "B-"
        case grade > 2.0:
            letterGrades[i] = "C+"
        case grade > 