count := 0
for _, num := range nums {
    if num > 10 {
        strNum := strconv.Itoa(num)
        firstDigit := strNum[0]
        lastDigit := strNum[len(strNum)-1]
        if (firstDigit == '1' || firstDigit == '3' || firstDigit == '5' || firstDigit == '7' || firstDigit == '9') &&
            (lastDigit == '1' || lastDigit == '3' || lastDigit == '5' || lastDigit == '7' || lastDigit == '9') {
            count++
        }
    }
}
return count
}


The function works by iterating over the array of numbers. For each number, it converts it to a string and gets the first and last characters. It then checks if the first and last characters are odd digits (1, 3, 5, 7, 9). If they are and the number itself is greater than 10, it increments the count. At the end, it returns the count.

*/

package main

import (
	"fmt"
)

func Specialfilter(nums []int) int {
	count := 0
	for _, num := range nums {
		if num > 10 {
			strNum := fmt.Sprintf("%d", num)
		