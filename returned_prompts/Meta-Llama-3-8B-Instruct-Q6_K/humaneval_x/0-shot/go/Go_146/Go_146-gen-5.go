Here is a solution in Go that uses a loop to iterate over the array and checks each number to see if it is greater than 10 and if both the first and last digits are odd:

```go
import (
    "strconv"
)

func Specialfilter(nums []int) int {
    var count int
    for _, num := range nums {
        str := strconv.Itoa(num)
        if num > 10 {
            if str[0]%2 != 0 && str[len(str)-1]%2 != 0 {
                count++
            }
        }
    }
    return count
}
```

In this code, `strconv.Itoa(num)` is used to convert the integer `num` to a string. Then we check if the first and last characters of the string are odd by using the modulus operator `%`. If the number is greater than 10 and both the first and last digits are odd, we increment the `count` variable. Finally, we return the `count` variable which holds the number of elements in the array that are greater than 10 and both first and last digits of a number are odd. 

Note: This function considers the absolute value of the number. If you want to consider the sign of the number as well, you can modify the condition as follows:
```go
if num > 10 && (num > 0 && str[0]%2 != 0 && str[len(str)-1]%2 != 0) || (num < 0 && str[0]%2 != 0 && str[len(str)-1]%2 != 0) {
    count++
}
```  This will consider only positive numbers with odd first and last digits or negative numbers with odd first and last digits.  If you want to consider only positive numbers, you can remove the part `(num < 0 && ...)` and if you want to consider only negative numbers, you can remove the part `(num > 0 && ...)`  If you want to consider both positive and negative numbers with odd first and last digits, you can remove the condition `num > 10` and the condition `(num > 0 && ...)` or `(num < 0 && ...)`  You can modify the condition according to your requirements. 