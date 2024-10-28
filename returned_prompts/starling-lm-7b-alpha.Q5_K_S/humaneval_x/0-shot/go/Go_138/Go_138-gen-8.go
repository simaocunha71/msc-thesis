To solve this problem, we can use the backtracking algorithm to find all the possible combinations of 4 even numbers to sum up to n, and then check if there are exactly four such numbers that sum up to n. Here is the step-by-step solution:

1. First, we define a function called findCombinations, which takes the number n and a slice of 4 integers as arguments. This function will recursively find all the possible combinations of 4 even numbers that sum up to n. It does this by iterating through all the possible values of the current number in the combination, and then recursively calling itself with the updated combination.

2. Next, we define a function called isSumOfFourEvenNumbers, which takes the number n as an argument. This function checks if there are exactly four even numbers that sum up to n. It does this by calling the findCombinations function with n and a slice of 4 zeros as arguments, and then checking if the sum of the four numbers in the combination is equal to n and if all the four numbers in the combination are even.

3. Finally, we can call the isSumOfFourEvenNumbers function with the given number n to check if it can be written as the sum of exactly four positive even numbers. If the function returns true, then n can be written as the sum of four positive even numbers, otherwise it cannot.

Here is the code for the solution:

```go
package main

import "fmt"

func findCombinations(n int, curCombination []int, result [][]int) {
    if len(curCombination) == 4 {
        sum := curCombination[0] + curCombination[1] + curCombination[2] + curCombination[3]
        if sum == n {
            result = append(result, curCombination)
        }
        return
    }

    for i := 0; i <= n; i += 2 {
        curCombination = append(curCombination, i)
        findCombinations(n, curCombination, result)
        curCombination = curCombination[:len(curCombination)-1]
    }
}

func isSumOfFourEvenNumbers(n int) bool {
    result :=