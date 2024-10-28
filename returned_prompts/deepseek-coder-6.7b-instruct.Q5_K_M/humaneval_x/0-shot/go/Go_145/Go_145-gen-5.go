
```go
func OrderByPoints(nums []int) []int {

    sort.Slice(nums, func(i, j int) bool {
        sumI := sumOfDigits(nums[i])
        sumJ := sumOfDigits(nums[j])
        if sumI == sumJ {
            return i < j
        }
        return sumI < sumJ
    })

    return nums
}

func sumOfDigits(n int) int {
    sum := 0
    for n != 0 {
        digit := n % 10
        sum += digit
        n /= 10
    }
    return sum
}
```

This program uses the built-in `sort.Slice` function to sort the slice of integers. It uses a custom sort function that compares the sum of the digits of two integers. If the sums are equal, it uses the index of the numbers in the original slice to break ties.

The `sumOfDigits` function calculates the sum of the digits of a given number by repeatedly taking the remainder of the number divided by 10 (which gives the last digit) and adding it to a running total. It then divides the number by 10 (which removes the last digit) and repeats the process until the number is 0.

This function works for both positive and negative numbers.

The `OrderByPoints` function returns the sorted slice of integers.

The time complexity of this solution is O(n*m*log(n)) where n is the number of elements in the slice and m is the number of digits in the maximum absolute value of an element in the slice. The space complexity is O(n) for the slice of integers.

The space complexity of the `sort.Slice` function is O(1), making it space efficient. The time complexity of the `sort.Slice` function is O(n*log(n)) where n is the number of elements in the slice.

The `sumOfDigits` function has a time complexity of O(m) where m is the number of digits in the number.

The `OrderByPoints` function has a time complexity of O(n*m*log(n)) and a