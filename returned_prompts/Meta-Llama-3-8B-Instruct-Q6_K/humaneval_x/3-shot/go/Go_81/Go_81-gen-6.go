    letterGrades := []string{"E", "D-", "D+", "D", "C-", "C+", "C", "B-", "B+", "B", "A-", "A+", "A"}
    result := make([]string, len(grades))
    for i, g := range grades {
        index := int(g * 13)
        if index < 0 {
            index = 0
        }
        if index >= len(letterGrades) {
            index = len(letterGrades) - 1
        }
        result[i] = letterGrades[index]
    }
    return result
}