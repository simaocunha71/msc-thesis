```go
package main

import "fmt"

func PairsSumToZero(l []int) bool {
    set := make(map[int]bool)
    for _, num := range l {
        if _, ok := set[-num]; ok {
            return true
        }
        set[num] = true
    }
    return false
}

func main() {
    fmt.Println(PairsSumToZero([]int{1, 3, 5, 0}))  // false
    fmt.Println(PairsSumToZero([]int{1, 3, -2, 1})) // false
    fmt.Println(PairsSumToZero([]int{1, 2, 3, 7})) // false
    fmt.Println(PairsSumToZero([]int{2, 4, -5, 3, 5, 7})) // true
    fmt.Println(PairsSumToZero([]int{1})) // false
}
```

This program defines a function `PairsSumToZero` that checks if there are two distinct elements in a list that sum to zero. It uses a map to store the elements of the list. For each element in the list, it checks if `-num` is already in the map. If it is, then there are two distinct elements that sum to zero, and the function returns `true`. If not, it adds `num` to the map. If the function finishes iterating over the list without finding two elements that sum to zero, it returns `false`.

The `main` function tests the `PairsSumToZero` function with different lists. It prints the result of calling `PairsSumToZero` with each list. The expected output is included in the comments. The program uses the `fmt.Println` function to print the results. The `main` function is the entry point of the program, and it is called when the program starts. The program uses the `package main` directive to specify the package name.

The time complexity of this program is O(n), where n is the length of the input list. This is because the program iterates over the list once, and each iteration takes constant time. The space complexity is also O(n), because the program uses a map to store the elements of the list. The map has at most n elements, so its size is proportional to the size of the input list.