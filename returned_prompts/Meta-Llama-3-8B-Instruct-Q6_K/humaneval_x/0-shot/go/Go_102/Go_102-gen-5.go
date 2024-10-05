```go
func ChooseNum(x, y int) int {
    if x%2 == 0 { // x is even
        if y%2 == 0 { // y is even
            if x > y { // x is greater than y
                return y
            } else { // x is less than or equal to y
                return x
            }
        } else { // y is odd
            if x <= y { // x is less than or equal to y
                return x
            } else { // x is greater than y
                return y - 1
            }
        }
    } else { // x is odd
        if y%2 == 0 { // y is even
            if x < y { // x is less than y
                return y
            } else { // x is greater than or equal to y
                return -1
            }
        } else { // y is odd
            if x <= y { // x is less than or equal to y
                return -1
            } else { // x is greater than y
                return y - 1
            }
        }
    }
}
```

This function works by first checking if x is even or odd, then checking if y is even or odd. It then compares the values of x and y to determine which one is the biggest even number within the range [x, y]. If no such number exists, it returns -1. The function handles all possible combinations of even and odd values of x and y. The time complexity of this function is O(1), as it only involves a few simple comparisons and arithmetic operations. The space complexity is O(1), as it only uses a constant amount of space to store the function's variables.