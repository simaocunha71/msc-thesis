
    filteredList := make([]string, 0)

    for _, str := range stringList {
        if strings.Contains(str, substring) {
            filteredList = append(filteredList, str)
        }
    }

    return filteredList
}

This function loops over the input list of strings and checks whether each string contains the given substring. If yes, it adds the string to the filtered list.

The function returns the filtered list of strings.

The function uses the `strings.Contains` function from the `strings` package to check if a string contains a substring.

The filtered list is initialized as an empty slice.

The `range` keyword is used to iterate over the input list of strings. For each string in the list, the `strings.Contains` function is called with the string and the substring as arguments. If the string contains the substring, it is added to the filtered list.
*/
package main

import (
	"fmt"
	"strings"
)

func FilterBySubstring(stringList []string, substring string) []string {
	filteredList := make([]string, 0)

	for _, str := range stringList {
		if strings.Contains(str, substring) {
			filteredList = append(filteredList, str)
		}
	}

	return filteredList
}

func main() {
	stringList := []string{"abc", "bacd", "cde", "array"}
	substring := "a"
	filteredList := FilterBySubstring(stringList, substring)
	fmt.Println(filteredList)
}

/*
Output:
[abc bacd array]
*/
package main

import (
	"fmt"
	"strings"
)

func main() {
	str := "Hello, World!"
	substr := "World"

	if strings.Contains(str, substr) {
		fmt.Printf("The string '%s' contains the substring '%s'.\n", str, substr)
	} else {
		fmt.Printf("The string '%s' does not contain the substring '%s