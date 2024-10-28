    
    result := make([]string, len(lst))

    for i, str := range lst {
        count := 0
        for _, ch := range str {
            if (ch-'0') % 2 != 0 {
                count++
            }
        }
        result[i] = fmt.Sprintf("the number of odd elements %don the string %d of the %dput.", count, count, count)
    }

    return result
}

The code first initializes an empty result list with the same length as the input list. Then, for each string in the input list, it counts the number of odd digits in the string. It then creates a string in the result list where each "i" is replaced with the count of odd digits.

The time complexity of this code is O(n*m) where n is the number of strings in the list and m is the average length of the strings. The space complexity is O(n) for the result list.
*/

package main

import (
	"fmt"
	"strings"
)

func OddCount(lst []string) []string {
	result := make([]string, len(lst))

	for i, str := range lst {
		count := 0
		for _, ch := range str {
			if (ch-'0')%2 != 0 {
				count++
			}
		}
		result[i] = fmt.Sprintf("the number of odd elements %don the string %d of the %dput.", count, count, count)
		result[i] = strings.ReplaceAll(result[i], "i", fmt.Sprintf("%d", count))
	}

	return result
}

func main() {
	fmt.Println(OddCount([]string{"1234567"}))
	fmt.Println(OddCount([]string{"3", "11111111"}))
}
package main

import (
	"fmt"
	"strings"
)

func OddCount(lst []string) []string {
	result := make([]string,