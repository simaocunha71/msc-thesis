    // Define a map of roman numerals to integers
    roman := map[int]string{
        1:    "i",
        4:    "iv",
        5:    "v",
        9:    "ix",
        10:   "x",
        40:   "xl",
        50:   "l",
        90:   "xc",
        100:  "c",
        400:  "cd",
        500:  "d",
        900:  "cm",
        1000: "m",
    }

    // Initialize result string
    result := ""

    // Loop through the roman map
    for value := range roman {

        // While the number is greater than or equal to the value,
        // append the corresponding roman numeral and subtract its value from the number
        for number >= value {
            result += roman[value]
            number -= value
        }

        // If the number is 0, return the result
        if number == 0 {
            return result
        }
    }

    // Return the result
    return result
}

*/

package main

import (
	"fmt"
	"strings"
)

func IntToMiniRoman(number int) string {

	roman := map[int]string{
		1000: "m",
		900:  "cm",
		500:  "d",
		400:  "cd",
		100:  "c",
		90:   "xc",
		50:   "l",
		40:   "xl",
		10:   "x",
		9:    "ix",
		5:    "v",
		4:    "iv",
		1:    "i",
	}

	result := ""

	for value := range roman {
		for number >= value {
			result += roman[value]
			number -= value
		}
		if number == 0 {
			return result
		}
	}

	return result
