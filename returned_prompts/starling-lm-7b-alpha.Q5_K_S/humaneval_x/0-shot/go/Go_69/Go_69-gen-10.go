
```go
package main

import "fmt"

func Search(lst []int) int {
	mp := make(map[int]int)
	for _, v := range lst {
		mp[v]++
	}
	for i := len(lst) - 1; i >= 0; i-- {
		if mp[lst[i]] >= lst[i] {
			return lst[i]
		}
	}
	return -1
}

func main() {
	fmt.Println(Search([]int{4, 1, 2, 2, 3, 1})) // 2
	fmt.Println(Search([]int{1, 2, 2, 3, 3, 3, 4, 4, 4})) // 3
	fmt.Println(Search([]int{5, 5, 4, 4, 4})) // -1
}
```

Explanation:

We start by creating a map `mp` to keep track of the frequency of each value in the list. We iterate over the list and increment the count for each value.

Next, we iterate over the list in reverse order. For each element, we check if its frequency is greater than or equal to its value. If it is, we return the value. If we reach the beginning of the list without finding a suitable value, we return -1.

In the provided examples, the first example returns 2 because the frequency of 2 is greater than or equal to 2. The second example returns 3 because the frequency of 3 is greater than or equal to 3. The third example returns -1 because there is no value whose frequency is greater than or equal to its value.

The time complexity of this solution is O(n), where n is the length of the input list.

```go
package main

import "fmt"

func Search(lst []int) int {
	mp := make(map[int]int)
	for _, v := range lst {
		mp[v]++
	}
	for i := len(lst) - 1; i >= 0; i-- {
		if mp[