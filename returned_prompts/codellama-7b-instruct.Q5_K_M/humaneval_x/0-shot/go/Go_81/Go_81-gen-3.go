
// It is the last week of the semester and the teacher has to give the grades
// to students. The teacher has been making her own algorithm for gradade.
// The only problem is, she has lost the code she used for grading.
// She has given you a list of GPAs for some students and you have to write
// a function that can output a list of letter grades using the following table:
// GPA       |    Letter grade
// 4.0                A+
// > 3.7                A
// > 3.3                A-
// > 3.0                B+
// > 2.7                B
// > 2.3                B-
// > 2.0                C+
// > 1.7                C
// > 1.3                C-
// > 1.0                D+
// > 0.7                D
// > 0.0                D-
// 0.0                E
// 
// 
// Example:
// grade_equation([4.0, 3, 1.7, 2, 3.5]) ==> ["A+", "B", "C-", "C", "A-"]
func NumericalLetterGrade(grades []float64) []string {
	var letterGrades []string
	for _, grade := range grades {
		switch {
		case grade >= 4.0:
			letterGrades = append(letterGrades, "A+")
		case grade >= 3.7:
			letterGrades = append(letterGrades, "A")
		case grade >= 3.3:
			letterGrades = append(letterGrades, "A-")
		case grade >= 3.0:
			letterGrades = append(letterGrades, "B+")
		case grade >= 2.7:
			letterGrades = append(letterGrades, "B")
		case grade >= 2.3:
			letterGrades = append(letterGrades, "B-")
		case grade >= 2.0:
			letterGr