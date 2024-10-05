The function first converts the input integer to a string. Then it iterates over the string, converting each character to an integer and checking if it is even or odd.

The '0' character is subtracted from each character to convert it to an integer. The int() function is not used because it would convert the Unicode code point of the character to an integer, not the numeric value of the character.

If the result of the subtraction is even, the count for even numbers is incremented. Otherwise, the count for odd numbers is incremented.

Finally, the function returns a tuple (an array in Go) of the counts for even and odd numbers.

The time complexity of this function is O(n), where n is the number of digits in the input integer. This is because it iterates over each digit of the integer once.

The space complexity is O(1), because the function only uses a fixed amount of space to store the counts for even and odd numbers, regardless of the size of the input integer.
*/

package main

import (
	"fmt"
)

func EvenOddCount(num int) [2]int {
	var result [2]int
	strNum := strconv.Itoa(num)
	for _, v := range strNum {
		if int(v-'0')%2 == 0 {
			result[0]++
		} else {
			result[1]++
		}
	}
	return result
}

func main() {
	fmt.Println(EvenOddCount(-12)) //[1 1]
	fmt.Println(EvenOddCount(123)) //[1 2]
}










































