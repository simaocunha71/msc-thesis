    r := regexp.MustCompile("(?i)[aeiou]")
    return r.ReplaceAllString(text, "")
}

*/

package main

import (
	"fmt"
	"regexp"
)

// RemoveVowels is a function that takes string and returns string without vowels.
func RemoveVowels(text string) string {
	r := regexp.MustCompile("(?i)[aeiou]")
	return r.ReplaceAllString(text, "")
}

func main() {
	fmt.Println(RemoveVowels(""))
	fmt.Println(RemoveVowels("abcdef\nghijklm"))
	fmt.Println(RemoveVowels("abcdef"))
	fmt.Println(RemoveVowels("aaaaa"))
	fmt.Println(RemoveVowels("aaBAA"))
	fmt.Println(RemoveVowels("zbcd"))
}
package main

import (
	"fmt"
	"testing"
)

func TestRemoveVowels(t *testing.T) {
	testCases := []struct {
		input string
		want  string
	}{
		{"", ""},
		{"abcdef\nghijklm", "bcdf\nghjklm"},
		{"abcdef", "bcdf"},
		{"aaaaa", ""},
		{"aaBAA", "B"},
		{"zbcd", "zbcd"},
	}

	for _, tc := range testCases {
		got := RemoveVowels(tc.input)
		if got != tc.want {
			t.Errorf("RemoveVowels(%s) = %s; want %s", tc.input, got, tc.want)
		}
	}
}

func ExampleRemoveVowels() {
	fmt.Println(RemoveVowels(""))
	fmt.Println(RemoveVowels("abcdef\nghijklm"))
	fmt.Println(RemoveVowels("abcdef"))
	fmt.Println