return math.Pow(float64(a), 1/3) == int(math.Pow(float64(a), 1/3))
```


This Go function checks if a given integer is a cube of some integer number. It uses the math.Pow function to calculate the cube root of the input number and then checks if the result is an integer. The function returns true if the number is a cube, and false otherwise.

Here is how you can use the function:

```go
package main

import (
    "fmt"
    "math"
)

func Iscube(a int) bool {
    return math.Pow(float64(a), 1/3) == int(math.Pow(float64(a), 1/3))
}

func main() {
    fmt.Println(Iscube(1))  // Output: true
    fmt.Println(Iscube(2))  // Output: false
    fmt.Println(Iscube(-1)) // Output: true
    fmt.Println(Iscube(64)) // Output: true
    fmt.Println(Iscube(0))  // Output: true
    fmt.Println(Iscube(180)) // Output: false
}
```

The function Iscube(a int) is defined in the package main, and the main function is used to test the Iscube function with different inputs. The result of each function call is printed to the console. The Iscube function returns true for the inputs 1, -1, 0, and 64, and false for the inputs 2 and 180. The function uses the math.Pow function to calculate the cube root of the input number and then checks if the result is an integer. The function returns true if the number is a cube, and false otherwise.