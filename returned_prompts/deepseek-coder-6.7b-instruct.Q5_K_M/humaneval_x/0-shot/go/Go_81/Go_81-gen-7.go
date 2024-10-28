
    // Initialize the list to store the letter grades
    var letterGrades []string

    // Iterate through the list of GPAs
    for _, gpa := range grades {

        // Determine the letter grade using a switch-case statement
        switch {
        case gpa == 4.0:
            letterGrades = append(letterGrades, "A+")
        case gpa > 3.7:
            letterGrades = append(letterGrades, "A")
        case gpa > 3.3:
            letterGrades = append(letterGrades, "A-")
        case gpa > 3.0:
            letterGrades = append(letterGrades, "B+")
        case gpa > 2.7:
            letterGrades = append(letterGrades, "B")
        case gpa > 2.3:
            letterGrades = append(letterGrades, "B-")
        case gpa > 2.0:
            letterGrades = append(letterGrades, "C+")
        case gpa > 1.7:
            letterGrades = append(letterGrades, "C")
        case gpa > 1.3:
            letterGrades = append(letterGrades, "C-")
        case gpa > 1.0:
            letterGrades = append(letterGrades, "D+")
        case gpa > 0.7:
            letterGrades = append(letterGrades, "D")
        case gpa > 0.0:
            letterGrades = append(letterGrades, "D-")
        default:
            letterGrades = append(letterGrades, "E")
        }
    }

    // Return the list of letter grades
    return letterGrades
}


*/

package main

import (
	"fmt"
)

func main() {
	grades := []float64{4.0, 3, 1.7, 2, 3.5}
	fmt.Println(NumericalLetterGrade(grades))
}

func NumericalLetterGrade(grades []float64) []string {
	var letterGrades []