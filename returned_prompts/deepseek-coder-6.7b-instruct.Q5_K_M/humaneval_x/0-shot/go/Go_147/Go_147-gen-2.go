
    // Your code here
    return 0
}

*/

package main

import "fmt"

func GetMaxTriples(n int) int {

	a := make([]int, n)
	for i := 1; i <= n; i++ {
		a[i-1] = i*i - i + 1
	}

	count := 0
	for i := 0; i < n-2; i++ {
		for j := i + 1; j < n-1; j++ {
			for k := j + 1; k < n; k++ {
				if (a[i]+a[j]+a[k])%3 == 0 {
					count++
				}
			}
		}
	}
	return count
}

func main() {
	fmt.Println(GetMaxTriples(5)) // Output: 1
}
/*
