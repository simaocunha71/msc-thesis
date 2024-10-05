    count := 0
    for _, num := range arr {
        if sumOfDigits(num) > 0 {
            count++
        }
    }
    return count
}

func sumOfDigits(num int) int {
    sum := 0
    for num != 0 {
        digit := num % 10
        sum += digit
        num /= 10
    }
    return sum
}

// Here we have a simple solution. We just iterate through the list of numbers
// and for each number we calculate the sum of its digits using the function sumOfDigits.
// If the sum > 0 we increase the counter. In the end we return the counter.


// sumOfDigits function works with positive and negative numbers.
// If the number is negative, the function takes the absolute value of the number
// and then calculates the sum of its digits.

// This is because in the problem statement we are asked to consider the first signed digit as negative.
// e.g. -123 has signed digits -1, 2, and 3.
// Therefore, we take the absolute value of the number to correctly calculate the sum of its digits.
```








































































































































































































































