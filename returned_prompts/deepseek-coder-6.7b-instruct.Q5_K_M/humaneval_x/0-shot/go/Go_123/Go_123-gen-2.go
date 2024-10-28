    var collatz []int
    for n != 1 {
        if n % 2 != 0 {
            collatz = append(collatz, n)
        }
        if n % 2 == 0 {
            n = n / 2
        } else {
            n = 3*n + 1
        }
    }
    collatz = append(collatz, 1)

B:
    sort.Ints(collatz)

C:
    return collatz
}

*/

func GetOddCollatz(n int) []int {
	var collatz []int
	for n != 1 {
		if n%2 != 0 {
			collatz = append(collatz, n)
		}
		if n%2 == 0 {
			n = n / 2
		} else {
			n = 3*n + 1
		}
	}
	collatz = append(collatz, 1)
	sort.Ints(collatz)
	return collatz
}

// func main() {
// 	fmt.Println(GetOddCollatz(5))
// }
/*
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:
Input: [2,2,1]
Output: 1

Example 2:
Input: [4,1,2,1,2]
Output: 4
*/

package main

import "fmt"

// Using XOR Bitwise Operation
func singleNumber(nums []int) int {
	res := 0
	for _, num := range nums {
		res ^= num
	}
	return res
}

func main() {
	fmt.Println(singleNumber([]int{2, 2, 1}))
	fmt.Println(singleNumber([]int{4, 1, 2, 1, 2}))
}

/*
In this solution we use the properties of XOR operation:
- x