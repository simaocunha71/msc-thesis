
	sum := 0
	
	for i, v := range lst {
		if i%2 == 0 && v%2 != 0 {
			sum += v
		}
	}
	
	return sum
}

*/
package main

import "fmt"

func main() {
	fmt.Println(Solution([]int{5, 8, 7, 1}))
	fmt.Println(Solution([]int{3, 3, 3, 3, 3}))
	fmt.Println(Solution([]int{30, 13, 24, 321}))
}
```
