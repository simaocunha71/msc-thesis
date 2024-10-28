
balance := 0

for _, operation := range operations {

balance += operation

if balance < 0 {

return true

}

}

return false

}

*/

package main

import "fmt"

func BelowZero(operations []int) bool {

	balance := 0

	for _, operation := range operations {

		balance += operation

		if balance < 0 {

			return true

		}

	}

	return false

}

func main() {

	fmt.Println(BelowZero([]int{1, 2, 3}))
	fmt.Println(BelowZero([]int{1, 2, -4, 5}))

}

// This program will return true if the balance falls below zero at any point during the operations and false otherwise.
// The operations array is a list of numbers representing the deposit and withdrawal operations.
// Each positive number is a deposit, while each negative number is a withdrawal.
// The function goes through each operation in the array, updates the balance accordingly and checks if the balance has dropped below zero.
// If it has, the function returns true, otherwise it returns false.

// Time complexity of the program is O(n), where n is the number of operations.
// Space complexity of the program is O(1), because it only uses a single variable to store the balance, regardless of the size of the input.

// This is a simple solution to the problem, but it assumes that the input is a list of integers. If the input can be of different types, additional error checking would be needed.

/*
Test case 1:

Input: [1, 2, 3]
Output: false

Test case 2:

Input: [1, 2, -4, 5]
Output: true

In this test case, the balance is 0 after the first two operations. After the third operation, the balance is -2. This falls below zero, so the function returns true.
*/
/*
