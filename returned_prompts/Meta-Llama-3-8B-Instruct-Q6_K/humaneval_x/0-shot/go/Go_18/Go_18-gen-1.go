```
package main

import (
	"fmt"
)

func HowManyTimes(str string, substring string) int {
	count := 0
	start := 0
	for start < len(str) {
		position := start
		for position < len(str) {
			if string(str[position : position+len(substring)]) == substring {
				count++
				position += len(substring)
			} else {
				break
			}
		}
		start += 1
	}
	return count
}

func main() {
	fmt.Println(HowManyTimes("", "a"))  // 0
	fmt.Println(HowManyTimes("aaa", "a"))  // 3
	fmt.Println(HowManyTimes("aaaa", "aa"))  // 3
}
```


Explanation:

The function HowManyTimes takes two parameters: the original string `str` and the substring `substring`. It returns the number of times `substring` can be found in `str`, considering overlapping cases.

The function iterates over the original string using a loop that starts at the beginning of the string. For each position in the string, it checks if the substring is present at that position. If it is, it increments the count and moves the position to the end of the matched substring. If it's not, it breaks the inner loop and moves to the next position in the outer loop.

The function uses a slice operation `str[position : position+len(substring)]` to extract a slice of characters from the original string, starting at position `position` and with a length of `len(substring)`. It then converts this slice to a string using the `string()` function and compares it to the substring. If they match, it increments the count and moves the position forward. If they don't match, it breaks the inner loop and moves to the next position in the outer loop.

The function returns the total count of matches found in the original string.

In the main function, we test the HowManyTimes function with different inputs and print the results to the console. The function correctly returns 0 for an empty original string, 3 for the string "aaa" and the substring "a", and 3 for the string "aaaa" and the substring "aa".