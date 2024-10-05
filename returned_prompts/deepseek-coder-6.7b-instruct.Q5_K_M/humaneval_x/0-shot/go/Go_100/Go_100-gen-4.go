
    result := make([]int, n)
    result[0] = n
    for i := 1; i < n; i++ {
        if result[i-1] % 2 == 0 {
            result[i] = result[i-1] + 2
        } else {
            result[i] = result[i-1] + 2
        }
    }
    return result
}


*/

package main

import (
	"fmt"
)

func MakeAPile(n int) []int {
	result := make([]int, n)
	result[0] = n
	for i := 1; i < n; i++ {
		if result[i-1]%2 == 0 {
			result[i] = result[i-1] + 2
		} else {
			result[i] = result[i-1] + 2
		}
	}
	return result
}

func main() {
	fmt.Println(MakeAPile(3))
}

/*
// Test cases:

Test Case 1:
Input:
3
Output:
[3,5,7]

Test Case 2:
Input:
5
Output:
[5,7,9,11,13]

Test Case 3:
Input:
10
Output:
[10,12,14,16,18,20,22,24,26,28,30]

Test Case 4:
Input:
1
Output:
[1]
*/
/*
