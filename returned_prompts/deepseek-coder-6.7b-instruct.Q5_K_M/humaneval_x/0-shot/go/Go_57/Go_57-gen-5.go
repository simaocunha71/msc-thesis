
    increase := 0
    decrease := 0

B:

    for i := 0; i < len(l) - 1; i++ {
        if l[i] < l[i+1] {
            increase += 1
        } else if l[i] > l[i+1] {
            decrease += 1
        }
    }

    if increase > 0 && decrease > 0 {
        return false
    }

    return true

}

```

**Explanation:**

This program checks if a given list of integers is monotonically increasing or decreasing. A list is said to be monotonically increasing if each subsequent number in the list is greater than the previous number. Conversely, a list is said to be monotonically decreasing if each subsequent number in the list is less than the previous number.

The function Monotonic takes a list of integers as input, then it initializes two counters increase and decrease to 0. It then iterates over the list, comparing each pair of integers. If it finds a pair where the first integer is less than the second, it increments the increase counter. If it finds a pair where the first integer is greater than the second, it increments the decrease counter.

Finally, it checks if either the increase counter or decrease counter is greater than 0. If both counters are greater than 0, it returns false because a list cannot be both monotonically increasing and monotonically decreasing. If only one counter is greater than 0, it returns true because a list is either monotonically increasing or decreasing.

**Test Cases:**

```go
package main

import (
	"fmt"
)

func main() {
	fmt.Println(Monotonic([]int{1, 2, 4, 20})) // true
	fmt.Println(Monotonic([]int{1, 20, 4, 10})) // false
	fmt.Println(Monotonic([]int{4, 1, 0, -10})) // true
}
```

**Output:**

```
true
false
true
```

The output matches the expected results in the problem statement.

---

###