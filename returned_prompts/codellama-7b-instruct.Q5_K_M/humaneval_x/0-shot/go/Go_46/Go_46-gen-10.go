
// This is my solution to the Fib4 problem.  I used a map to store the values of the Fib4 sequence as I computed them.
// The map stores the index of the Fib4 number sequence (0, 1, 2, 3, ...) as the key and the value is the computed value of the Fib4 number sequence for that index.
// I used a loop to compute the Fib4 number sequence for each index in the map.
// I then used a loop to print out the Fib4 number sequence.

// The time complexity is O(n) because I am looping n times to print out the Fib4 number sequence.
// The space complexity is O(n) because I am storing the values of the Fib4 number sequence in a map.

// This solution is not efficient because I am using a map and a loop to compute the Fib4 number sequence.
// I would use recursion to compute the Fib4 number sequence.  Recursion is more efficient than a loop.
// I would also use a slice to store the values of the Fib4 number sequence instead of a map.  This would be more efficient because a slice has a fixed size.

package main

import "fmt"

func main() {

	// Create a map to store the values of the Fib4 number sequence.
	m := make(map[int]int)

	// Compute the Fib4 number sequence for each index in the map.
	for i := 0; i <= 10; i++ {
		m[i] = fib4(i)
	}

	// Print out the Fib4 number sequence.
	for i := 0; i <= 10; i++ {
		fmt.Println(m[i])
	}
}

// This is my solution to the Fib4 problem.  I used a map to store the values of the Fib4 sequence as I computed them.
// The map stores the index of the Fib4 number sequence (0, 1, 2, 3, ...) as the key and the value is the computed value of the Fib4 number sequence for that index.
// I used a loop to compute the Fib4 number sequence for each index in the map.