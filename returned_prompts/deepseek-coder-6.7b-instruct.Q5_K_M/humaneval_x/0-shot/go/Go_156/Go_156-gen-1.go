    roman := ""
    values := []int{1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1}
    symbols := []string{"m", "cm", "d", "cd", "c", "xc", "l", "xl", "x", "ix", "v", "iv", "i"}

    for i := 0; i < len(values); i++ {
        for number >= values[i] {
            roman += symbols[i]
            number -= values[i]
        }
    }

    return roman
}

*/

package main

import (
	"fmt"
)

func main() {
	fmt.Println(IntToMiniRoman(19))  // "xix"
	fmt.Println(IntToMiniRoman(152)) // "clii"
	fmt.Println(IntToMiniRoman(426)) // "cdxxvi"
}

func IntToMiniRoman(number int) string {
	roman := ""
	values := []int{1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1}
	symbols := []string{"m", "cm", "d", "cd", "c", "xc", "l", "xl", "x", "ix", "v", "iv", "i"}

	for i := 0; i < len(values); i++ {
		for number >= values[i] {
			roman += symbols[i]
			number -= values[i]
		}
	}

	return roman
}
package main

import (
	"fmt"
	"strings"
)

func main() {
	fmt.Println(ReverseWords("Hello World"))
	fmt.Println(ReverseWords("I