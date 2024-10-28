    return strings.FieldsFunc(s, func(c rune) bool {
        return c == ',' || c == ' '
    })
}

*/

package main

import (
	"fmt"
	"strings"
)

func WordsString(s string) []string {
	return strings.FieldsFunc(s, func(c rune) bool {
		return c == ',' || c == ' '
	})
}

func main() {
	fmt.Println(WordsString("Hi, my name is John"))
	fmt.Println(WordsString("One, two, three, four, five, six"))
}

/*
Output:
[Hi my name is John]
[One two three four five six]
*/

// This program splits the string into words based on commas or spaces. It uses the strings.FieldsFunc function to do this, which splits the string at each run of characters that satisfy the function. In this case, the function checks if the character is a comma or a space.
// The result is an array of words, which is then returned by the function.

// Also, it's important to note that the strings.FieldsFunc function considers multiple spaces and commas as a single separator. So, if there are multiple spaces or commas in a row, it will consider it as a single separator.
// For example, in the string "Hi,    my  name  is   John", the words will be ["Hi", "my", "name", "is", "John"].
// Similarly, in the string "One,, two,,, three,,, four,,, five,,, six", the words will be ["One", "two", "three", "four", "five", "six"].
// This is why the output of the program matches the expected output in the problem statement.

// The main function is just for testing the WordsString function. It calls the function with two strings, and prints the resulting arrays of words.
// The output of the main function should match the expected output in the problem statement.
