
    // create a map to store the conversion from GPA to letter grade
    gradeTable := map[float64]string{
        4.0: "A+",
        3.7: "A",
        3.3: "A-",
        3.0: "B+",
        2.7: "B",
        2.3: "B-",
        2.0: "C+",
        1.7: "C",
        1.3: "C-",
        1.0: "D+",
        0.7: "D",
        0.0: "D-",
    }

    // create a variable to store the result
    letterGrades := make([]string, 0, len(grades))

    // iterate over the list of GPAs
    for _, gpa := range grades {
        // find the corresponding letter grade
        letterGrade, ok := gradeTable[gpa]
        if !ok {
            // if the GPA is less than 0.7, the grade is "E"
            letterGrade = "E"
        }
        // append the letter grade to the result
        letterGrades = append(letterGrades, letterGrade)
    }
    // return the list of letter grades
    return letterGrades
}

*/

package main

import (
	"fmt"
)

func NumericalLetterGrade(grades []float64) []string {

	gradeTable := map[float64]string{
		4.0: "A+",
		3.7: "A",
		3.3: "A-",
		3.0: "B+",
		2.7: "B",
		2.3: "B-",
		2.0: "C+",
		1.7: "C",
		1.3: "C-",
		1.0: "D+",
		0.7: "D",
		0.0: "D-",
	}

	letterGrades := make([]string, 0, len(grades))

	for _, gpa := range grades {