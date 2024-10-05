
}

I know the problem is asking to return a sorted list of numbers with all unique digits, but I don't know how to start. I am thinking I will need to convert each integer to a string, then iterate through the string to check for even digits. But this doesn't seem like a good solution.

A: You're on the right track, but you can use a map to track the unique digits. Here's how you can do it:

```go
func UniqueDigits(x []int) []int {
    var res []int
    digitMap := make(map[int]bool)

    for _, num := range x {
        strNum := strconv.Itoa(num)
        hasEven := false

        for _, ch := range strNum {
            digit, _ := strconv.Atoi(string(ch))
            if digit%2 == 0 {
                hasEven = true
                break
            }
        }

        if !hasEven && !digitMap[num] {
            res = append(res, num)
            digitMap[num] = true
        }
    }

    sort.Ints(res)
    return res
}
```

This function iterates over each number in the input slice. It converts the number to a string and then iterates over each character in the string. If any character is an even number, it sets the `hasEven` variable to true and breaks out of the loop.

If `hasEven` is still false (which means no even digits were found) and the number hasn't been seen before (checked with `digitMap`), it adds the number to the result slice and marks it as seen in the map.

Finally, it sorts the result slice and returns it.

This solution assumes that the input slice only contains positive integers. If this isn't the case, you'll need to add error checking to handle invalid inputs.





























































