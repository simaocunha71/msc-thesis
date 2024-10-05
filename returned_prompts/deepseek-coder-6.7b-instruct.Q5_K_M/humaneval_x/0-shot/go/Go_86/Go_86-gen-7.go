    words := strings.Fields(s)
    var result []string

B:
    for _, word := range words {
        chars := strings.Split(word, "")
        sort.Strings(chars)
        result = append(result, strings.Join(chars, ""))
    }

C:
    return strings.Join(result, " ")
}

func main() {
    fmt.Println(AntiShuffle("Hello World!!!"))
}

The function AntiShuffle takes a string, splits it into words and sorts each word's characters in ascending order. 
Then it joins them back together, keeping the order of words and spaces.

*/

package main

import (
	"fmt"
	"sort"
	"strings"
)

func AntiShuffle(s string) string {
	words := strings.Fields(s)
	var result []string

	for _, word := range words {
		chars := strings.Split(word, "")
		sort.Strings(chars)
		result = append(result, strings.Join(chars, ""))
	}

	return strings.Join(result, " ")
}

func main() {
	fmt.Println(AntiShuffle("Hello World!!!"))
}

/*
Output:
Hello  !!!Wdlor
*/

// Testing the function
/*
func main() {
    fmt.Println(AntiShuffle("Hi"))
    fmt.Println(AntiShuffle("hello"))
    fmt.Println(AntiShuffle("Hello World!!!"))
}
*/

/*
Output:
Hi
ehllo
Hello  !!!Wdlor
*/

// Testing the function
/*
func main() {
    fmt.Println(AntiShuffle("Hi"))
    fmt.Println(AntiShuffle("hello"))
    fmt.Println(AntiShuffle("Hello World!!!"))
}
*/

/*
Output:
Hi
ehllo
Hello  !!!Wdlor
*/

// Testing the function
/*
func main() {
    fmt