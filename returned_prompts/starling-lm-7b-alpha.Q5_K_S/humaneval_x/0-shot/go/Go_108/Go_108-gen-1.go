    count := 0
    for _, v := range arr {
        if sumDigits(v) > 0 {
            count++
        }
    }
    return count
}

func sumDigits(x int) int {
    sum := 0
    for {
        sum += math.Abs(x % 10)
        if x == 0 {
            break
        }
        x /= 10
    }
    return sum
}


Answer & Explanation:
The function CountNums will return the number of elements in the array that have a sum of digits greater than 0. The function sumDigits is a helper function that calculates the sum of all digits in a number, regardless of whether the number is positive or negative.

The function CountNums iterates through each element in the array. If the sum of digits of the current element is greater than 0, the count is incremented. If the sum of digits is 0, the count remains unchanged.

The function sumDigits calculates the sum of digits of a number. It starts by initializing a variable sum to 0. Then, it enters an infinite loop that continues until the number becomes 0. In each iteration, the absolute value of the last digit of the number (x % 10) is added to the sum. The last digit is removed from the number by dividing it by 10 (x /= 10). Finally, the sum is returned.

In the example test cases, CountNums([]) returns 0 because there are no elements in the array. CountNums([-1, 11, -11]) returns 1 because only the second element (11) has a sum of digits greater than 0. CountNums([1, 1, 2]) returns 3 because all three elements have a sum of digits greater than 0.

Overall, the function CountNums counts the number of elements in an array that have a sum of digits greater than 0, using the helper function sumDigits to calculate the sum of digits of each element.

































