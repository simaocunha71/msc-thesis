
func CanArrange(arr []int) int {
    max := -1
    for i, e := range arr {
        if i == 0 || e > arr[i-1] {
            max = i
        }
    }
    return max
}


























```

```

```
```

```go
package main

import (
	"fmt"
)

func main() {
	fmt.Println(CanArrange([]int{1, 2, 4, 3, 5}))
}

func CanArrange(arr []int) int {
	max := -1
	for i, e := range arr {
		if i == 0 || e > arr[i-1] {
			max = i
		}
	}
	return max
}
```
```

```python
def CanArrange(arr):
    max = -1
    for i, e in enumerate(arr):
        if i == 0 or e > arr[i-1]:
            max = i
    return max
```
```

```
```

```

```
```

```java
public class Main {
    public static void main(String[] args) {
        System.out.println(CanArrange(new int[]{1, 2, 4, 3, 5}));
    }

    public static int CanArrange(int[] arr) {
        int max = -1;
        for (int i = 0; i < arr.length; i++) {
            if (i == 0 || arr[i] > arr[i - 1]) {
                max = i;
            }
        }
        return max;
    }
}
```
```

```

```
```

```

```go
package main

import (
	"fmt"
)

func main() {
	fmt.Println(CanArrange([]int{1,