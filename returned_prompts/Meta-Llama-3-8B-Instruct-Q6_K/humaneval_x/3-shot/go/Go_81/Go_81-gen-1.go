    letter_grades := []string{"A+", "A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "D-", "E"}
    result := make([]string, 0)
    for _, g := range grades {
        for i, cut := range []float64{4.0, 3.7, 3.3, 3.0, 2.7, 2.3, 2.0, 1.7, 1.3, 1.0, 0.7, 0.0} {
            if g >= cut {
                result = append(result, letter_grades[i])
                break
            }
        }
    }
    return result
}