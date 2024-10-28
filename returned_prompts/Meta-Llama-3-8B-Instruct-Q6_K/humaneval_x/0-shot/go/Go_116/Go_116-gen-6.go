```go
func SortArray(arr []int) []int {
    sort.Slice(arr, func(i, j int) bool {
        ones1, _ := countOnes(arr[i])
        ones2, _ := countOnes(arr[j])
        if ones1 != ones2 {
            return ones1 < ones2
        }
        return arr[i] < arr[j]
    })
    return arr
}

func countOnes(n int) (int, int) {
    count := 0
    for n > 0 {
        n = n & (n - 1)
        count++
    }
    return count, 0
}
```



Explanation:

The task is to sort an array of non-negative integers based on the number of ones in their binary representation in ascending order. If the number of ones is the same, then the array should be sorted based on the decimal value.

To solve this, we use the `sort.Slice` function from the `sort` package in Go. This function sorts the array according to a comparison function. The comparison function takes two indices `i` and `j` and returns `true` if the element at index `i` should come before the element at index `j` in the sorted array.

In our comparison function, we first count the number of ones in the binary representation of the elements at indices `i` and `j` using the `countOnes` function. If the number of ones is different, we return `true` if `i` has fewer ones or `false` if `i` has more ones. If the number of ones is the same, we return `true` if `arr[i]` is less than `arr[j]`.

The `countOnes` function counts the number of ones in the binary representation of a number by performing a bitwise AND operation with the number and subtracting 1 until the number becomes 0.

Here is the complete code:

```go
func SortArray(arr []int) []int {
    sort.Slice(arr, func(i, j int) bool {
        ones1, _ := countOnes(arr[i])
        ones2, _ := countOnes(arr[j])
        if ones1 != ones2 {
            return ones1 < ones2
        }
        return arr[i] < arr[j]
    })
    return arr
}

func countOnes(n int) (int, int) {
    count := 0
    for n > 0 {
        n