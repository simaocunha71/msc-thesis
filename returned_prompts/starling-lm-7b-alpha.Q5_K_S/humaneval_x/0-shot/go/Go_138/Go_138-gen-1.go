To solve this problem, we can use backtracking to find out whether there exist 4 even numbers that can sum up to the given number n. 

Here's the step by step explanation of the solution:

1. Initialize a result variable to false, which indicates whether the target number can be written as the sum of exactly 4 positive even numbers.
2. Start from 2, and use a for loop to iterate through all possible even numbers. If the loop size is 4, it means we have found all 4 even numbers.
3. Use another for loop to iterate through all possible combinations of 4 even numbers. The outer loop starts from the second even number, since the first even number has already been considered.
4. Inside the inner for loop, calculate the sum of the 4 even numbers, and check if it is equal to the target number. If it is, set the result to true and break the inner for loop.
5. After the outer for loop, check the result. If it is true, return true. Otherwise, return false.

The time complexity of this solution is O(n^4), where n is the target number. The space complexity is O(1), as we only use a few variables in the function.

Here's an implementation of the above approach:

func IsEqualToSumEven(n int) bool {
    result := false

    for i := 2; i <= n; i += 2 {
        for j := i + 2; j <= n; j += 2 {
            for k := j + 2; k <= n; k += 2 {
                for l := k + 2; l <= n; l += 2 {
                    if i + j + k + l == n {
                        result = true
                        break
                    }
                }
                if result {
                    break
                }
            }
            if result {
                break
            }
        }
        if result {
            break
        }
    }

    return result
}

You can use this function to check whether a given number can be written as the sum of exactly 4 positive even numbers.

For example, if you call the function with n = 8, it will return true, as 