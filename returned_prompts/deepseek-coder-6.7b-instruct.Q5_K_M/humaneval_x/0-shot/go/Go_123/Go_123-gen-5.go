    collatz := make([]int, 0, n)
    collatz = append(collatz, n)

B:
    for collatz[len(collatz)-1] != 1 {
        if collatz[len(collatz)-1]%2 == 0 {
            collatz = append(collatz, collatz[len(collatz)-1]/2)
        } else {
            collatz = append(collatz, collatz[len(collatz)-1]*3+1)
        }
    }

C:
    sort.Ints(collatz)
    return collatz
}

*/

package collatz

import (
	"sort"
)

// Given a positive integer n, return a sorted list that has the odd numbers in collatz sequence.
func GetOddCollatz(n int) []int {
	collatz := make([]int, 0, n)
	collatz = append(collatz, n)

	for collatz[len(collatz)-1] != 1 {
		if collatz[len(collatz)-1]%2 == 0 {
			collatz = append(collatz, collatz[len(collatz)-1]/2)
		} else {
			collatz = append(collatz, collatz[len(collatz)-1]*3+1)
		}
	}

	sort.Ints(collatz)
	return collatz
}

// This function uses the Collatz conjecture to generate a sequence of numbers, then filters out the even numbers and returns the sorted list.
// The Collatz conjecture is a conjecture in mathematics that concerns a sequence defined as follows:
// start with any positive integer n. Then each term is obtained from the previous term as follows:
// if the previous term is even, the next term is one half of the previous term.
// if the previous term is odd, the next term is 3 times the previous term plus 1.
// The conjecture is that no matter what value of n, the sequence will always reach 1.
// The returned list is sorted in increasing order.
// The function