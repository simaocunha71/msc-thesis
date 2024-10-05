
	gradeMap := make(map[float64]string)
	gradeMap[4.0] = "A+"
	gradeMap[3.7] = "A"
	gradeMap[3.3] = "A-"
	gradeMap[3.0] = "B+"
	gradeMap[2.7] = "B"
	gradeMap[2.3] = "B-"
	gradeMap[2.0] = "C+"
	gradeMap[1.7] = "C"
	gradeMap[1.3] = "C-"
	gradeMap[1.0] = "D+"
	gradeMap[0.7] = "D"
	gradeMap[0.0] = "D-"
	gradeMap[0.0] = "E"

	var letterGrades []string

	for _, grade := range grades {
		for gpa, letterGrade := range gradeMap {
			if grade >= gpa {
				letterGrades = append(letterGrades, letterGrade)
				break
			}
		}
	}

	return letterGrades
}

// 