You can use the following code to solve this problem:

```go
func LargestSmallestIntegers(lst []int) [2]interface{} {
    var largestNegative int
    var smallestPositive int
    var hasNegative bool
    var hasPositive bool

    for _, num := range lst {
        if num < 0 {
            if !hasNegative || num > largestNegative {
                largestNegative = num
            }
            hasNegative = true
        } else if num > 0 {
            if !hasPositive || num < smallestPositive {
                smallestPositive = num
            }
            hasPositive = true
        }
    }

    if hasNegative {
        return [2]interface{}{largestNegative, nil}
    } else if hasPositive {
        return [2]interface{}{nil, smallestPositive}
    } else {
        return [2]interface{}{nil, nil}
    }
}
```

Explanation:

1. We initialize `largestNegative` and `smallestPositive` variables to keep track of the largest negative and smallest positive integers in the list.
2. We also initialize `hasNegative` and `hasPositive` booleans to check if there are any negative or positive integers in the list.
3. We iterate through the list and update `largestNegative` and `smallestPositive` variables if we find a larger negative or smaller positive integer.
4. Finally, we return a tuple `[2]interface{}` containing `largestNegative` and `smallestPositive` if they exist, otherwise we return `(nil, nil)`.