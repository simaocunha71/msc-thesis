
max := l[0]
for _, v := range l {
    if v > max {
        max = v
    }
}
return max
}
```

### Python:

```python
# Python

def MaxElement(l):
    return max(l)
```

## Problem 2: Minimum element in a list

### Go:

```go
package main

import (
	"fmt"
	"math"
)

func MinElement(l []int) int {
	min := math.MaxInt64
	for _, v := range l {
		if v < min {
			min = v
		}
	}
	return min
}

func main() {
	fmt.Println(MinElement([]int{1, 2, 3}))                     // 1
	fmt.Println(MinElement([]int{5, 3, -5, 2, -3, 3, 9, 0, 123})) // -5
}
```

### JavaScript:

```javascript
// JavaScript

function MinElement(l) {
    return Math.min(...l);
}

console.log(MinElement([1, 2, 3]));    // 1
console.log(MinElement([5, 3, -5, 2])); // -5
```

### Python:

```python
# Python

def MinElement(l):
    return min(l)

print(MinElement([1, 2, 3]))          # 1
print(MinElement([5, 3, -5, 2]))      # -5
```

## Problem 3: Sum of elements in a list

### Go:

```go
package main

import "fmt"

func SumElements(l []int) int {
	sum := 0
	for _, v := range l {
		sum += v
	}
	return sum
}

func main() {
	fmt.Println(SumElements([]int{1, 2, 3}))       // 6
	fmt.Println(SumElements([]int{5, 