You can solve this problem by iterating through the two lists and checking the parity of each number. If a number in lst1 is odd, you need to check if there is an even number in lst2 to swap with it. If there is, you swap the two numbers and continue. If there isn't, you return "NO". If you reach the end of lst1 without needing to swap any numbers, you return "YES".

Here is the Go code to solve the problem:

```go
func Exchange(lst1, lst2 []int) string {
    for _, num := range lst1 {
        if num % 2 != 0 {
            found := false
            for i, num2 := range lst2 {
                if num2 % 2 == 0 {
                    lst1 = append(lst1[:i], lst1[i+1:]...)
                    lst2 = append(lst2[:i], append([]int{num}, lst2[i:]...)...)
                    found = true
                    break
                }
            }
            if !found {
                return "NO"
            }
        }
    }
    return "YES"
}
```

This code first checks if a number in lst1 is odd. If it is, it then checks if there is an even number in lst2 to swap with it. If there is, it swaps the two numbers and continues. If there isn't, it returns "NO". If it reaches the end of lst1 without needing to swap any numbers, it returns "YES".