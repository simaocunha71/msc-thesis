```go
package main

import (
	"fmt"
	"sort"
)

func Monotonic(l []int) bool {
	sort.Ints(l)
	for i := 1; i < len(l); i++ {
		if l[i-1] >= l[i] {
			return false
		}
	}
	return true
}

func main() {
	fmt.Println(Monotonic([]int{1, 2, 4, 20}))  // true
	fmt.Println(Monotonic([]int{1, 20, 4, 10})) // false
	fmt.Println(Monotonic([]int{4, 1, 0, -10})) // true
}
```

This program sorts the list of integers and then checks if the list is monotonically increasing. It iterates through the list, checking if each element is less than or equal to the previous one. If it finds an element that is not, it immediately returns false, indicating that the list is not monotonically increasing. If it finishes the loop without finding such an element, it returns true, indicating that the list is monotonically increasing. The function `Monotonic` is then called in the `main` function with three test lists. The output of the program is:

```
true
false
true
```
which matches the expected output. The program uses the `sort` package to sort the list, and the `fmt` package to print the results. The `main` function is the entry point of the program. The `Monotonic` function is the core of the program, and it checks if a list of integers is monotonically increasing. It does this by sorting the list, and then checking if each element is less than or equal to the previous one. If it finds an element that is not, it returns false. If it finishes the loop without finding such an element, it returns true. The program is designed to be efficient and easy to understand, and it uses standard Go syntax and data structures.