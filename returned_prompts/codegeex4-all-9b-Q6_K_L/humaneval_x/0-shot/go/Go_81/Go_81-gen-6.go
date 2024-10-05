func NumericalLetterGrade(grades []float64) []string {
	letter := []string{}
	for _, g := range grades {
		switch {
		case g == 4.0:
			letter = append(letter, "A+")
		case g > 3.7:
			letter = append(letter, "A")
		case g > 3.3:
			letter = append(letter, "A-")
		case g > 3.0:
			letter = append(letter, "B+")
		case g > 2.7:
			letter = append(letter, "B")
		case g > 2.3:
			letter = append(letter, "B-")
		case g > 2.0:
			letter = append(letter, "C+")
		case g > 1.7:
			letter = append(letter, "C")
		case g > 1.3:
			letter = append(letter, "C-")
		case g > 1.0:
			letter = append(letter, "D+")
		case g > 0.7:
			letter = append(letter, "D")
		case g > 0.0:
			letter = append(letter, "D-")
		default:
			letter = append(letter, "E")
		}
	}
	return letter
}