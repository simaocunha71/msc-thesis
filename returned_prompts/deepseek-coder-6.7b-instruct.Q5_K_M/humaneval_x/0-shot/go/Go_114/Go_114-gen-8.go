    total := 0
    min := math.MaxInt64

    for _, num := range nums {
        total += num
        if total < min {
            min = total
        }
        total = int(math.Max(float64(total), float64(num)))
    }

    return min
}

The above function is a solution to the problem, but I'm not sure why it's incorrect. I would appreciate any help.

A: The problem is that the line where you reset total to num if total is less than min is incorrect.
Instead of:
total = int(math.Max(float64(total), float64(num)))

it should be:
total = int(math.Max(float64(total+num), float64(num)))

This will ensure that total always includes the current number being evaluated, not just the maximum of the current number and total.
Here's the corrected code:
import (
    "math"
)

func Minsubarraysum(nums []int) int {
    total := 0
    min := math.MaxInt64

    for _, num := range nums {
        total += num
        if total < min {
            min = total
        }
        total = int(math.Max(float64(total+num), float64(num)))
    }

    return min
}

This will now correctly calculate the minimum subarray sum.

A: The problem is in this line:
total = int(math.Max(float64(total), float64(num)))

You're resetting total to the maximum of the current total and num, but you don't want to do that if num is negative. If num is negative, adding it to total could potentially decrease the total, which is what you want to happen.
What you want to do is add num to total and then take the maximum of the old total and the new total. Here's how you can do that:
total = int(math.Max(float64(total+num), float64(total)))

This will ensure that total is always the maximum of either the sum of the current number and the old