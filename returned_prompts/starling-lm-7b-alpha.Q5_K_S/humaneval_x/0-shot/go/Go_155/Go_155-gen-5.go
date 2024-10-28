    var (
        even    int
        odd     int
        numStr  string
    )

    numStr = strconv.Itoa(num)

    for i := 0; i < len(numStr); i++ {
        if numStr[i] % 2 == 0 {
            even++
        } else {
            odd++
        }
    }

    return [2]int{even, odd}
}

In this code, we convert the integer to a string, and then traverse the string to count the number of even and odd digits respectively.
This is a very simple and straightforward solution, and can be used directly.

But if the number is very large, for example, 1234567891011121314151617181920, at this time, we need to optimize the solution.

For large numbers, we can directly calculate the number of even and odd digits without converting to a string. Here is a more optimized solution:

func EvenOddCount(num int) (even, odd int) {
    for num > 0 {
        if num%10%2 == 0 {
            even++
        } else {
            odd++
        }
        num /= 10
    }
    return
}

This solution is based on the fact that the last digit of the number is the unit place, and the last two digits represent 10 times the unit place.

For example, if we want to count the number of even and odd digits in the number 1234567891011121314151617181920, we can directly calculate as follows:

1234567891011121314151617181920
12345678910111213141516171819
2345678910111213141516171819
3456789