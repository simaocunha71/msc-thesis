
    replace := strings.Replace(text, "  ", "-", -1)
    replace = strings.Replace(replace, " ", "_", -1)
    if strings.HasPrefix(replace, "-") {
        replace = "_" + replace[1:]
    }
	return replace
}

// Test case
func main() {
	fmt.Println(FixSpaces("Example"))         // Example
	fmt.Println(FixSpaces("Example 1"))       // Example_1
	fmt.Println(FixSpaces(" Example 2"))      // _Example_2
	fmt.Println(FixSpaces(" Example  3"))     // _Example-3
}
```

The above code works by first replacing all instances of two consecutive spaces with a "-". Then it replaces all instances of a single space with an underscore. If the final string starts with a "-", it prepends an underscore to the string.

The complexity of the code is O(n) where n is the length of the string.

The test cases validate that the function is working as expected.

It's worth mentioning that this code assumes that there are no instances of three or more consecutive spaces. If there are, the function will not work correctly.

If you need to handle such cases, you would need to use a more complex regex-based approach.

Also, if you need to handle other special characters, you can change the `" "` and `"  "` in the replace function to the character you want to replace.

Lastly, this code is case sensitive. If you need it to be case insensitive, you could add a `ToLower()` or `ToUpper()` function call to the `text` variable before the replace functions.
*/
package main

import (
	"fmt"
	"strings"
)

func FixSpaces(text string) string {
	replace := strings.Replace(text, "  ", "-", -1)
	replace = strings.Replace(replace, " ", "_", -1)
	if strings.HasPrefix(replace, "-") {
		replace = "_" + replace[1:]
	}
	return replace
}

func main() {
	fmt.Println(FixSpaces("