
// It is the last week of the semester and the teacher has to give the grades
// to students. The teacher has been making her own algorithm for grading.
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
	if len(grades) == 0 {
		return nil
	}

	grades = make([]int, len(grades))
	for i, g := range grades {
		grades[i] = float64ToInt(g) // 4.0 => 4, 3.7 => 3
	}

	ret := []string{"", "", "C+"}
	for grades[len(grades)-1] >= 2 {
		ret = append(ret, strconv.FormatFloat(float64ToInt(grades[len(grades)-1]), 'f', -1, 64))
	} else if grades[len(grades)-1] > 0.7 { // >= 2 is a special case
		ret = append(ret, "C+")
	} else {
		ret = append(ret