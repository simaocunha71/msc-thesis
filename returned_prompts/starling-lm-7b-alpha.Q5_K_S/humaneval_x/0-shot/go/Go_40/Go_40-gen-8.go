
Here's a solution in Go:

```go
package main

import (
	"fmt"
)

func TriplesSumToZero(l []int) bool {
	for i := 0; i < len(l)-2; i++ {
		for j := i + 1; j < len(l)-1; j++ {
			for k := j + 1; k < len(l); k++ {
				if l[i]+l[j]+l[k] == 0 {
					return true
				}
			}
		}
	}
	return false
}

func main() {
	fmt.Println(TriplesSumToZero([]int{1, 3, 5, 0}))
	fmt.Println(TriplesSumToZero([]int{1, 3, -2, 1}))
	fmt.Println(TriplesSumToZero([]int{1, 2, 3, 7}))
	fmt.Println(TriplesSumToZero([]int{2, 4, -5, 3, 9, 7}))
	fmt.Println(TriplesSumToZero([]int{1}))
}
```

And here's a solution in Python:

```python
def TriplesSumToZero(l):
	for i in range(len(l)-2):
		for j in range(i+1, len(l)-1):
			for k in range(j+1, len(l)):
				if l[i] + l[j] + l[k] == 0:
					return True
	return False
```

You can test this code by using the `python -m doctest test.py` command.

```python
"""
>> TriplesSumToZero([1, 3, 5, 0])
False
>> TriplesSumToZero([1, 3, -2, 1])
True
>> TriplesSumToZero([1, 2, 3, 7])
False
>> TriplesSumToZero([2