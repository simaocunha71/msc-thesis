
    // The collision of two cars is the same as the collision of n-1 cars and 1 car.
    // So the total number of collisions is the sum of the collisions of n cars and the 
    // sum of the collisions of n-1 cars.
    // This recursively continues until n equals 1.
    // The base case is when n equals 1, there are 0 collisions.

    // Pseudo code:
    // if n == 1:
    //     return 0
    // else:
    //     return n-1 + CarRaceCollision(n-1)

    // In code:

    if n == 1 {
        return 0
    } else {
        return n - 1 + CarRaceCollision(n - 1)
    }
}

// The function works by recursively calling itself with a decrementing value of n,
// each time adding the current value of n to the total.  This is effectively
// summing the number of collisions for each pair of cars that collide, and thus
// giving the total number of collisions.
//
// This function runs in O(n) time, as each recursive call adds another function call,
// and the function calls are added up to n.  This is the best time complexity we can achieve for this problem.
//
// The function also runs in O(n) space, as each recursive call adds another layer to the call stack,
// and the maximum depth of the call stack is n.  This is the best space complexity we can achieve for this problem.
//
// The function assumes that the input is a positive integer.  If the input is not a positive integer,
// the function may not behave as expected.

*/
package main

import (
	"fmt"
)

func CarRaceCollision(n int) int {
	if n == 1 {
		return 0
	} else {
		return n - 1 + CarRaceCollision(n-1)
	}
}

func main() {
	fmt.Println(CarRaceCollision(10))
}

// This function is used to calculate the number of collisions in a car race.
// The function takes an integer n as