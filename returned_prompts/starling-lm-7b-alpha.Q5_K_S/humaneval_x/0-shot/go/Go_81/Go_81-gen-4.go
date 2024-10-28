
func NumericalLetterGrade(grades []float64) []string {
	result := make([]string, len(grades))
	for i, grade := range grades {
		if grade > 4.0 {
			result[i] = "A+"
		} else if grade > 3.7 {
			result[i] = "A"
		} else if grade > 3.3 {
			result[i] = "A-"
		} else if grade > 3.0 {
			result[i] = "B+"
		} else if grade > 2.7 {
			result[i] = "B"
		} else if grade > 2.3 {
			result[i] = "B-"
		} else if grade > 2.0 {
			result[i] = "C+"
		} else if grade > 1.7 {
			result[i] = "C"
		} else if grade > 1.3 {
			result[i] = "C-"
		} else if grade > 1.0 {
			result[i] = "D+"
		} else if grade > 0.7 {
			result[i] = "D"
		} else if grade > 0.0 {
			result[i] = "D-"
		} else {
			result[i] = "E"
		}
	}
	return result
}

Answer:

It is the last week of the semester and the teacher has to give the grades
to students. The teacher has been making her own algorithm for grading.
The only problem is, she has lost the code she used for grading.
She has given you a list of GPAs for some students and you have to write
a function that can output a list of letter grades using the following table:

GPA       |    Letter grade
4.0                A+
> 3.7                A
> 3.3                A-
> 3.0                B+
