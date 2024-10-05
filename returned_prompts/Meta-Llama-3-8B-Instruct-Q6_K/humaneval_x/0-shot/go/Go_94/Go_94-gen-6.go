```go
package main

import (
    "fmt"
    "math"
    "strconv"
)

func Skjkasdkd(lst []int) int {
    var maxPrime int
    for _, num := range lst {
        if num > 1 {
            for i := 2; i <= int(math.Sqrt(float64(num))); i++ {
                if num%i == 0 {
                    break
                }
            }
            if i > int(math.Sqrt(float64(num))) {
                if maxPrime < num {
                    maxPrime = num
                }
            }
        }
    }
    sum := 0
    for _, digit := range strconv.Itoa(maxPrime) {
        sum += int(digit - '0')
    }
    return sum
}

func main() {
    lst := []int{0, 3, 2, 1, 3, 5, 7, 4, 5, 5, 5, 2, 181, 32, 4, 32, 3, 2, 32, 324, 4, 3}
    fmt.Println(Skjkasdkd(lst))  // Output: 10
}
```



The solution is to iterate through the list of integers, check if each number is a prime, and keep track of the largest one. Then, convert the largest prime to a string and calculate the sum of its digits. Here is a sample implementation in Go:

```go
package main

import (
    "fmt"
    "math"
    "strconv"
)

func Skjkasdkd(lst []int) int {
    var maxPrime int
    for _, num := range lst {
        if num > 1 {
            for i := 2; i <= int(math.Sqrt(float64(num))); i++ {
                if num%i == 0 {
                    break
                }
            }
            if i > int(math.Sqrt(float64(num))) {
                if maxPrime < num {
                    maxPrime = num
                }
            }
        }
    }
    sum := 0
    for _, digit := range strconv.Itoa(maxPrime) {
        sum += int(digit - '0')
    }
    return sum
}

func main() {
    lst := []int{0, 3, 2, 1, 3, 5, 7, 4, 5, 5, 5, 2, 181, 32, 