
The problem lies in the condition check for first and last digit. You are checking if the firstDigit is equal to "1", "3", etc., and then you check if the lastDigit is equal to "1", "3", etc. 

This is incorrect because you're checking if firstDigit is equal to "1", "3", etc. and then you're checking if lastDigit is equal to "1", "3", etc. This means that if the first digit is "9" for example, you'd still check if the last digit is "1", "3", etc., which is not what you want.

You should use the logical OR operator (||) to check both conditions together. Also, the negative sign "-" in front of "1", "3", etc. is not necessary.

Here's the corrected code:

```go
import  (
    "strconv"
)

func Specialfilter(nums []int) int  {
    var count int = 0
    for _, num := range nums {
        if num > 10 {
            strNum := strconv.Itoa(num)
            firstDigit := strNum[0:1]
            lastDigit := strNum[len(strNum)-1:]
            if (firstDigit == "1" || firstDigit == "3" || firstDigit == "5" || firstDigit == "7" || firstDigit ==