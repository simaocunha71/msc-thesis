
// First, we initialize a variable count to store the number of times the substring appears in the string.
    count := 0

// Next, we loop through the string.
    for i := 0; i < len(str)-len(substring)+1; i++ {

// Inside the loop, we check if the substring appears at the current index i.
        if str[i:i+len(substring)] == substring {

// If the substring appears, we increment the count.
            count++
        }
    }

// Finally, we return the count.
    return count
}
*/

import (
	"fmt"
	"strings"
)

func HowManyTimes(str string, substring string) int {
	count := strings.Count(str, substring)
	return count
}

func main() {
	fmt.Println(HowManyTimes("", "a"))         // 0
	fmt.Println(HowManyTimes("aaa", "a"))      // 3
	fmt.Println(HowManyTimes("aaaa", "aa"))    // 3
	fmt.Println(HowManyTimes("banananobanana", "ana")) // 3
}
package main

import (
	"fmt"
	"strings"
)

// 