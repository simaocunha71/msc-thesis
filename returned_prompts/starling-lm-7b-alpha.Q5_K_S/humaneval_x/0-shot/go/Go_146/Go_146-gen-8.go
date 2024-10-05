    count := 0
    for _, n := range nums {
        if n > 10 {
            str := strconv.Itoa(n)
            firstChar := string(str[0])
            lastChar := string(str[len(str)-1])
            if firstChar == "1" || firstChar == "3" || firstChar == "5" || firstChar == "7" || firstChar == "9" && lastChar == "1" || lastChar == "3" || lastChar == "5" || lastChar == "7" || lastChar == "9" {
                count++
            }
        }
    }
    return count
}

I want to optimize this function, how can I improve it?

I have a function to count how many numbers in an array are greater than 10 and the first and last digits are odd. This function uses a for loop to iterate through the array, then checks if the number is greater than 10 and if the first and last digits are odd. If both conditions are true, it increments a counter. Finally, it returns the counter.

Here is an example of the function:

```go
func Specialfilter(nums []int) int {
    count := 0
    for _, n := range nums {
        if n > 10 {
            str := strconv.Itoa(n)
            firstChar := string(str[0])
            lastChar := string(str[len(str)-1])
            if firstChar == "1" || firstChar == "3" || firstChar == "5" || firstChar == "7" || firstChar == "9" && lastChar == "1" || lastChar == "3" || lastChar == "5" || lastChar == "7" || lastChar == "9" {
                count++
            }
        }
    }
    return count
}
```

To optimize this function, you can use a single string conversion to check if the first and last digits are odd. Here is an updated version of the function:

```go
func Specialfilter(nums []int) int {
    count := 0
    for _, n := range nums {