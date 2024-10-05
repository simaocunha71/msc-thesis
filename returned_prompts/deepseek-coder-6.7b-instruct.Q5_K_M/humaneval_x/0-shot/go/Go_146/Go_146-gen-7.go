    count := 0

    for _, num := range nums {
        if num > 10 {
            str := strconv.Itoa(num)
            first := str[0:1]
            last := str[len(str)-1:]

            if first == "1" || first == "3" || first == "5" || first == "7" || first == "9" {
                if last == "1" || last == "3" || last == "5" || last == "7" || last == "9" {
                    count++
                }
            }
        }
    }

    return count
}

The function Specialfilter loops through the input array nums and checks each number. If the number is greater than 10, it converts the number to a string and checks the first and last characters. If both characters are odd (1, 3, 5, 7, or 9), it increments count by 1. Finally, it returns count.

The function strconv.Itoa is used to convert int to string. The first and last characters are obtained by slicing the string. The comparison is done with string values because Go doesn't support direct comparison of string to int.
*/
package main

import (
	"fmt"
)

func Specialfilter(nums []int) int {
	count := 0
	for _, num := range nums {
		if num > 10 {
			str := fmt.Sprintf("%d", num)
			first := str[0:1]
			last := str[len(str)-1:]
			if first == "1" || first == "3" || first == "5" || first == "7" || first == "9" {
				if last == "1" || last == "3" || last == "5" || last == "7" || last == "9" {
					count++
				}
			}
		}
	}
	return count
}

func main() {
	fmt.Println(Specialfilter([]int{15, -73, 14, -15}))
	fmt.Println(Specialfilter([]int{3