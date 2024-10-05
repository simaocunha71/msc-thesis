Here is the solution:

```go
import (
    "strconv"
)

func AddElements(arr []int, k int) int {
    var sum int
    for i := 0; i < k; i++ {
        str := strconv.Itoa(arr[i])
        if len(str) <= 2 {
            num, _ := strconv.Atoi(str)
            sum += num
        }
    }
    return sum
}
```

Explanation:
The problem asks to find the sum of the elements with at most two digits from the first k elements of the array. 

We iterate over the first k elements of the array. For each element, we convert it to a string and check if the length of the string is less than or equal to 2. This means the element has at most two digits. If it does, we convert the string back to an integer and add it to the sum.

Finally, we return the sum. 

The time complexity is O(k) because we iterate over the first k elements of the array. The space complexity is O(1) because we only use a constant amount of space to store the sum and the temporary string. 