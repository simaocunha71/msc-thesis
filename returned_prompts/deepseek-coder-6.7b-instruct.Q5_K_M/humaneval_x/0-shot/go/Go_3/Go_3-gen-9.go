
balance := 0

for _, op := range operations {
    balance += op
    if balance < 0 {
        return true
    }
}

return false
}


This function works by iterating over the operations array, adding each operation to the balance, and then checking if the balance is less than zero at any point. If it is, the function immediately returns true. If it doesn't find such an operation, it returns false.
*/

package main

import (
	"fmt"
)

func BelowZero(operations []int) bool {
	balance := 0
	for _, op := range operations {
		balance += op
		if balance < 0 {
			return true
		}
	}
	return false
}

func main() {
	operations1 := []int{1, 2, 3}
	operations2 := []int{1, 2, -4, 5}

	fmt.Println(BelowZero(operations1)) // false
	fmt.Println(BelowZero(operations2)) // true
}
package main

import (
	"fmt"
	"strconv"
)

func main() {
	testCases := []struct {
		input    int
		expected string
	}{
		{1, "1"},
		{2, "11"},
		{3, "21"},
		{4, "1211"},
		{5, "111221"},
		{6, "312211"},
		{7, "13112221"},
	}

	for _, tc := range testCases {
		actual := lookAndSay(tc.input)
		if actual != tc.expected {
			fmt.Printf("FAIL: lookAndSay(%d) expected %s, got %s\n", tc.input, tc.expected, actual)
		} else {
			fmt.Printf("PASS: lookAndSay(%d) = %s\n", tc.input, actual)
		}
	}
}

func lookAndSay(n