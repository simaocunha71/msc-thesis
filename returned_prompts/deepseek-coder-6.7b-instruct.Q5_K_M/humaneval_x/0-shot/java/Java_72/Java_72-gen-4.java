
	sum:= 0
	for i:=0; i < len(lst); i += 2 {
		if lst[i] % 2 != 0 {
			sum += lst[i]
		}
	}
	return sum
}

func main() {
	fmt.Println(Solution([]int{5, 8, 7, 1}))
	fmt.Println(Solution([]int{3, 3, 3, 3, 3}))
	fmt.Println(Solution([]int{30, 13, 24, 321}))
}

// Output:
// 12
// 9
// 0
*/

//Explanation:
//In the first example, the odd elements in the even positions are 5 (at position 0) and 1 (at position 3). Their sum is 12.
//In the second example, all elements are odd and at even positions, so the sum is 9.
//In the third example, there are no odd elements in even positions, so the sum is 0.
//The solution uses a for loop to iterate over the list, skipping every other element (i += 2). It then checks if the current element is odd (lst[i] % 2 != 0) and if so, adds it to the sum. Finally, it returns the sum.

//Code:

package main

import "fmt"

func Solution(lst []int) int {
	sum := 0
	for i := 0; i < len(lst); i += 2 {
		if lst[i]%2 != 0 {
			sum += lst[i]
		}
	}
	return sum
}

func main() {
	fmt.Println(Solution([]int{5, 8, 7, 1}))      // Output: 12
	fmt.Println(Solution([]int{3, 3, 3, 3, 3}))    // Output: 9
	fmt.Println(Solution([]int{30, 13, 24, 321}))   // Output