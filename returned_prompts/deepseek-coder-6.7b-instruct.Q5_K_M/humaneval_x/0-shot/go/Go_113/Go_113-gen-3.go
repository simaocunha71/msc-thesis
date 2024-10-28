    var result []string
    for _, v := range lst {
        count := 0
        for _, c := range v {
            if (int(c)-'0')%2 != 0 {
                count++
            }
        }
        str := fmt.Sprintf("the number of odd elements %don the str%ng %d of the %dnput.", count, count, count, count)
        result = append(result, str)
    }
    return result
}

*/

func OddCount(lst []string) []string {

	var result []string
	for i, v := range lst {
		count := 0
		for _, c := range v {
			if int(c-'0')%2 != 0 {
				count++
			}
		}
		str := fmt.Sprintf("the number of odd elements %don the string %d of the input.", count, i+1)
		result = append(result, str)
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
	"math"
)

// 