```
func NumericalLetterGrade(grades []float64) []string {
    letterGrades := make([]string, 0)
    for _, g := range grades {
        if g >= 4.0 {
            letterGrades = append(letterGrades, "A+")
        } else if g > 3.7 {
            letterGrades = append(letterGrades, "A")
        } else if g > 3.3 {
            letterGrades = append(letterGrades, "A-")
        } else if g > 3.0 {
            letterGrades = append(letterGrades, "B+")
        } else if g > 2.7 {
            letterGrades = append(letterGrades, "B")
        } else if g > 2.3 {
            letterGrades = append(letterGrades, "B-")
        } else if g > 2.0 {
            letterGrades = append(letterGrades, "C+")
        } else if g > 1.7 {
            letterGrades = append(letterGrades, "C")
        } else if g > 1.3 {
            letterGrades = append(letterGrades, "C-")
        } else if g > 1.0 {
            letterGrades = append(letterGrades, "D+")
        } else if g > 0.7 {
            letterGrades = append(letterGrades, "D")
        } else if g > 0.0 {
            letterGrades = append(letterGrades, "D-")
        } else {
            letterGrades = append(letterGrades, "E")
        }
    }
    return letterGrades
}
```



The code above defines a function `NumericalLetterGrade` that takes a slice of floats (`grades`) as input and returns a slice of strings (`letterGrades`). The function iterates over each grade in the input slice and appends the corresponding letter grade to the `letterGrades` slice based on the GPA ranges defined in the problem statement. The function returns the `letterGrades` slice at the end.

In the example provided, the function is called with the input `grades := []float64{4.0, 3, 1.7, 2, 3.5}` and returns `["A+", "B", "C-", "C", "A-"]`.