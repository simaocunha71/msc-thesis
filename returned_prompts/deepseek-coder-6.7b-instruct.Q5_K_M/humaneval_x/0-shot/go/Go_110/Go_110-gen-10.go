
	count := 0
	for i := 0; i < len(lst1); i++ {
		if lst1[i] % 2 != 0 {
			for j := 0; j < len(lst2); j++ {
				if lst2[j] % 2 == 0 {
					count++
					break
				}
			}
		}
	}
	if count >= len(lst1) / 2 {
		return "YES"
	}
	return "NO"
}

// In the above code, we first count the number of odd numbers in lst1.
// Then for every odd number, we try to find an even number in lst2.
// If we can find an even number in lst2 for every odd number in lst1,
// it means we can make all numbers in lst1 even by swapping.
// If the count of such numbers is greater than or equal to half of the total
// number of odd numbers in lst1, we return "YES", otherwise "NO".
// This solution works in O(n^2) time complexity.
```


```go
package main

import (
	"fmt"
)

func Exchange(lst1, lst2  []int) string {
	odd1, odd2, even2 := 0, 0, 0

	for i := 0; i < len(lst1); i++ {
		if lst1[i] % 2 != 0 {
			odd1++
		}
	}

	for i := 0; i < len(lst2); i++ {
		if lst2[i] % 2 == 0 {
			even2++
		} else {
			odd2++
		}
	}

	if odd1 > odd2 + even2 {
		return "NO"
	}
	return "YES"
}

func main() {
	fmt.Println(Exchange([]int{1, 2, 3, 4}, []int{1, 2, 3, 4})) // YES
	fmt.Println(Exchange([]int{1, 2, 