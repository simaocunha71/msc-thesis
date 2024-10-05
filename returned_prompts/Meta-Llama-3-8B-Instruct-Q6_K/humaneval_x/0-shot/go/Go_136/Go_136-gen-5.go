```go
package main
import "fmt"
func LargestSmallestIntegers(lst []int) [2]interface{} {
    var maxNegative, minPositive int
    var hasNegative, hasPositive bool

    for _, num := range lst {
        if num < 0 {
            if !hasNegative {
                hasNegative = true
            }
            if maxNegative < num {
                maxNegative = num
            }
        } else if num > 0 {
            if !hasPositive {
                hasPositive = true
            }
            if minPositive == 0 || num < minPositive {
                minPositive = num
            }
        }
    }

    if !hasNegative {
        maxNegative = 0
    }
    if !hasPositive {
        minPositive = 0
    }

    if maxNegative == 0 && minPositive == 0 {
        return [2]interface{}{nil, nil}
    } else if maxNegative == 0 {
        return [2]interface{}{nil, minPositive}
    } else if minPositive == 0 {
        return [2]interface{}{maxNegative, nil}
    } else {
        return [2]interface{}{maxNegative, minPositive}
    }
}

func main() {
    fmt.Println(LargestSmallestIntegers([]int{2, 4, 1, 3, 5, 7}))  // (nil, 1)
    fmt.Println(LargestSmallestIntegers([]int{}))              // (nil, nil)
    fmt.Println(LargestSmallestIntegers([]int{0}))             // (nil, nil)
}
```
The function LargestSmallestIntegers takes a list of integers as input and returns a tuple (a, b) where 'a' is the largest negative integer and 'b' is the smallest positive integer. If there are no negative or positive integers, it returns them as nil. The function iterates over the list of integers and checks for negative and positive numbers separately. It keeps track of the maximum negative number and the minimum positive number. If no negative or positive numbers are found, it initializes the respective variables to 0. Finally, it checks the values of maxNegative and minPositive and returns the appropriate tuple. In the main function, the function is called with different lists of integers and the results are printed. The output is as expected.