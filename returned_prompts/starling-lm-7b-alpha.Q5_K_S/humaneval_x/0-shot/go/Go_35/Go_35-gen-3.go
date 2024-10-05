
To find the maximum element in a list, we can use the built-in max function in Go. Here's how you can define and use the MaxElement function:

```go
package main

import (
    "fmt"
)

func MaxElement(l []int) int {
    return max(l...)
}

func main() {
    fmt.Println(MaxElement([]int{1, 2, 3})) // 3
    fmt.Println(MaxElement([]int{5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10})) // 123
}
```

In the MaxElement function, we use the max function to find the maximum value in the list. The max function takes variable number of arguments (represented by "...") and returns the maximum value among them. We pass the list as arguments to the max function to find the maximum element.

In the main function, we call the MaxElement function with two different lists and print the result.

The output of the program will be:

```
3
123
```

This means that the maximum element in the first list is 3, and the maximum element in the second list is 123.

Note that the max function is part of the Go standard library, so you don't need to import any additional packages to use it.

I hope this helps! Let me know if you have any more questions.

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

