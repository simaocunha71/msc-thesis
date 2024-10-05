    var letterGrades = []string{"E", "D-", "D", "D+", "C-", "C", "C+", "B-", "B", "B+", "A-", "A", "A+"}
    var gradePoints = []float64{0.0, 0.3, 0.7, 1.0, 1.3, 1.7, 2.0, 2.3, 2.7, 3.0, 3.3, 3.7, 4.0}

    var result = make([]string, len(grades))

    for i, grade := range grades {
        for j := 0; j < len(gradePoints); j++ {
            if grade >= gradePoints[j] {
                result[i] = letterGrades[j]
                break
            }
        }
    }

    return result
}



