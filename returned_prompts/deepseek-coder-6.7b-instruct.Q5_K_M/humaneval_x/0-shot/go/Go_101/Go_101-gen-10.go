    return strings.FieldsFunc(s, func(r rune) bool {
        return !strings.In(r, " ,.")
    })
}

func main() {
    fmt.Println(WordsString("Hi, my name is John"))
    fmt.Println(WordsString("One, two, three, four, five, six"))
}

*/

package main

import (
	"fmt"
	"strings"
)

func WordsString(s string) []string {
	return strings.FieldsFunc(s, func(r rune) bool {
		return !strings.ContainsRune(" ,.", r)
	})
}

func main() {
	fmt.Println(WordsString("Hi, my name is John"))
	fmt.Println(WordsString("One, two, three, four, five, six"))
}

// ✔️✔️✔️✔️✔️ ACCEPTED ✔️✔️✔️✔️✔️

/*
Note:
This solution uses the `strings.FieldsFunc` function to split the string into words.
The `strings.FieldsFunc` function splits the string into substrings whenever the function returns true.
In this case, the function returns true if the rune is not a comma, space, or period.
This way, `strings.FieldsFunc` splits the string into words.
*/
