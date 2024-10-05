
	// Make an array to store the letter grades
	letterGrades := make([]string, len(grades))

	// Iterate over the grades
	for i, grade := range grades {
		// If the grade is greater than 4, it's an error
		if grade > 4 {
			letterGrades[i] = "E"
		} else if grade >= 3.7 {
			letterGrades[i] = "A+"
		} else if grade >= 3.3 {
			letterGrades[i] = "A"
		} else if grade >= 3 {
			letterGrades[i] = "A-"
		} else if grade >= 2.7 {
			letterGrades[i] = "B+"
		} else if grade >= 2.3 {
			letterGrades[i] = "B"
		} else if grade >= 2 {
			letterGrades[i] = "B-"
		} else if grade >= 1.7 {
			letterGrades[i] = "C+"
		} else if grade >= 1.3 {
			letterGrades[i] = "C"
		} else if grade >= 1 {
			letterGrades[i] = "C-"
		} else if grade >= 0.7 {
			letterGrades[i] = "D+"
		} else if grade >= 0 {
			letterGrades[i] = "D"
		} else if grade < 0 {
			letterGrades[i] = "D-"
		}
	}
	return letterGrades
}

// NumericalLetterGrade2
func NumericalLetterGrade2(grades []float64) []string {
	// Make an array to store the letter grades
	letterGrades := make([]string, len(grades))
	// Iterate over the grades
	for i, grade := range grades {
		switch {
		case