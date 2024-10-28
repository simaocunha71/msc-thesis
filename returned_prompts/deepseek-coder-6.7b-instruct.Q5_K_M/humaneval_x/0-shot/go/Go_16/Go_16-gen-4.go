    count :=0
    str = strings.ToLower(str)
    check := make(map[rune]int)

    for _, letter := range str {
        if _, ok := check[letter]; !ok {
            check[letter] = 1
            count++
        }
    }
    return count
}


func main() {
    fmt.Println(CountDistinctCharacters("xyzXYZ"))  // Outputs: 3
    fmt.Println(CountDistinctCharacters("Jerry"))   // Outputs: 4
}

This code works by converting the input string to lower case and then iterating over each character in the string. If a character is not already in the map, it is added to the map and the count is incremented. The final count is returned as the result.
*/

package main

import (
	"fmt"
	"strings"
)

func CountDistinctCharacters(str string) int {
	count := 0
	str = strings.ToLower(str)
	check := make(map[rune]int)

	for _, letter := range str {
		if _, ok := check[letter]; !ok {
			check[letter] = 1
			count++
		}
	}
	return count
}

func main() {
	fmt.Println(CountDistinctCharacters("xyzXYZ")) // Outputs: 3
	fmt.Println(CountDistinctCharacters("Jerry"))  // Outputs: 4
}

// Outputs:
// 3
// 4
// Process finished with exit code 0

/*
In the code, we use a map to keep track of the distinct characters in the string. The key in the map is the character and the value is not important (we just use it as a flag to indicate if the character is in the map or not). The count of distinct characters is incremented every time a new character is added to the map.
*/

/*
The time complexity of the code is O(n), where n is the length of the string. This is because we are iterating over the string once. The space complexity is also O(n), where n is the length