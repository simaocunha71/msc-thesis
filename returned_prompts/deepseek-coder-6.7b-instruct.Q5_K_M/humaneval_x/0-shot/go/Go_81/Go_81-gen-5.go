
	letters := []string{}

	for _, grade := range grades {
		switch {
		case grade == 4.0:
			letters = append(letters, "A+")
		case grade > 3.7:
			letters = append(letters, "A")
		case grade > 3.3:
			letters = append(letters, "A-")
		case grade > 3.0:
			letters = append(letters, "B+")
		case grade > 2.7:
			letters = append(letters, "B")
		case grade > 2.3:
			letters = append(letters, "B-")
		case grade > 2.0:
			letters = append(letters, "C+")
		case grade > 1.7:
			letters = append(letters, "C")
		case grade > 1.3:
			letters = append(letters, "C-")
		case grade > 1.0:
			letters = append(letters, "D+")
		case grade > 0.7:
			letters = append(letters, "D")
		case grade > 0.0:
			letters = append(letters, "D-")
		default:
			letters = append(letters, "E")
		}
	}

	return letters
}

*/
package main

import (
	"fmt"
)

func NumericalLetterGrade(grades []float64) []string {

	letters := []string{}

	for _, grade := range grades {
		switch {
		case grade == 4.0:
			letters = append(letters, "A+")
		case grade > 3.7:
			letters = append(letters, "A")
		case grade > 3.3:
			letters = append(letters, "A-")
		case grade > 3.0:
			letters = append(letters, "B+")
		case grade > 2.7:
			letters = append(