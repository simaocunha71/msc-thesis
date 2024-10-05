
// BelowZero([]int{1, 2, 3})
// false
// BelowZero([]int{1, 2, -4, 5})
// true
func BelowZero(operations []int) bool {
	var balance int
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

// Your task is to complete the function BelowZero.

// Input Format

// You need to complete the function BelowZero that takes an array as its only argument.

// Output Format

// You need to return true or false denoting whether the balance of the account fell below zero at any point during the operations.

// Sample Test Case

// Sample Input

// 1. BelowZero([1, 2, 3])
// 2. BelowZero([1, 2, -4, 5])
// Expected Output

// Output 1:
// false
// Output 2:
// true

// Sample Output

// false
// true

// Explanation

// Explanation

// Explanation 1:

// The operations are as follows:

// Initial balance: 0
// 1: balance += 1 => balance = 1
// 2: balance += 2 => balance = 3
// 3: balance += 3 => balance = 6

// There is no point at which the balance fell below zero.

// Explanation 2:

// The operations are as follows:

// Initial balance: 0
// 1: balance += 1 => balance = 1
// 2: balance += 2 => balance = 3
// 3: balance -= 4 => balance = -1
// 4: balance += 5 => balance = 4

// There is a point at which the balance fell below zero.

// Constraints

//