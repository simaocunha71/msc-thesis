    var filteredList  []string

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

    fmt.Println(FilterBySubstring(stringList, substring))

}

This function works by iterating over each string in the input list. It checks if the current string contains the given substring using the strings.Contains function. If the string contains the substring, it's added to the filteredList.

The final filteredList is returned at the end of the function.

This function is case-sensitive. If you want it to be case-insensitive, you can convert both the string and substring to lowercase before checking if they contain each other.
*/

import (
	"strings"
)

// Filter an input list of strings only for ones that contain given substring
func FilterBySubstring(stringList []string, substring string) []string {

	var filteredList []string

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

	fmt.Println(FilterBySubstring(stringList, substring))

}

// Output:
// [abc bacd array]

/*
The strings.Contains function is used to check if the string contains the substring. If it does, the string is added to the filteredList.

The final filteredList is returned at the end of the function.

This function is case-sensitive. If you want it to be case-insensitive, you can convert both the string and substring to lowercase before checking if they contain each other.
*/

/*
