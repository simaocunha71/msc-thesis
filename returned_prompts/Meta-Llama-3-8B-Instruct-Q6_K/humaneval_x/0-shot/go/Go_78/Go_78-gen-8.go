```go
func HexKey(num string) int {
    count := 0
    primes := []int{2, 3, 5, 7, 11, 13, 17, 19}
    for _, c := range num {
        switch {
        case '0' <= c && c <= '9':
            digit := int(c - '0')
        case 'A' <= c && c <= 'F':
            digit := int(c - 'A' + 10)
        }
        if contains(primes, digit) {
            count++
        }
    }
    return count
}

func contains(arr []int, target int) bool {
    for _, v := range arr {
        if v == target {
            return true
        }
    }
    return false
}
```


In this problem, we are required to write a function that takes a hexadecimal number as a string and counts the number of hexadecimal digits that are prime numbers. The hexadecimal digits are 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F. The prime numbers are 2, 3, 5, 7, 11, 13, 17, ... . So, we have to determine the number of the following digits: 2, 3, 5, 7, B, D.

Here is the solution in Go:

We first define a function `HexKey` that takes a hexadecimal number as a string and counts the number of hexadecimal digits that are prime numbers. We use a slice `primes` to store the prime numbers. We then iterate over each character in the input string. If the character is a digit (0-9), we subtract the ASCII value of '0' to get the decimal value of the digit. If the character is a letter (A-F), we subtract the ASCII value of 'A' and add 10 to get the decimal value of the digit. We then use the `contains` function to check if the decimal value of the digit is in the `primes` slice. If it is, we increment the `count` variable. Finally, we return the `count` variable.

The `contains` function is a helper function that checks if a target value is in a slice. It iterates over each value in the slice and returns `true` if the target value is found,