    var result int = 0
    for _, v := range lst {
        result += int(math.Ceil(v)) * int(math.Ceil(v))
    }
    return result
}

Answer:
func SumSquares(lst []float64) int {

    var result int = 0
    for _, v := range lst {
        result += int(math.Ceiling(v)) * int(math.Ceiling(v))
    }
    return result
}

Explanation:
We need to return the sum of squared numbers in the given list, so we start by initializing a variable called result to 0. Then we use a for loop to iterate through each element in the lst slice. Inside the loop, we use the math.Ceiling() function to round each element to the upper integer value, and then multiply it by itself to get the square. Finally, we add the result of each squared number to the result variable. After the loop is finished, we return the final result.

To round a float64 value to the upper integer, we use the math.Ceiling() function. This function takes a float64 value as an argument and returns the smallest integer greater than or equal to that value. We apply this function to each element in the lst slice, and then multiply the result by itself to get the square. We add the result of each squared number to the result variable.

Finally, we return the result, which is the sum of the squared numbers in the given list, rounded to the upper integer.

Overall, the function SumSquares takes a slice of float64 values as an argument, calculates the sum of squared numbers in the given list, rounds each element to the upper integer, and returns the result as an int.

This solution meets the requirements of the problem, as it correctly calculates the sum of squared numbers in the given list, rounds each element to the upper integer, and returns the result as an int.

Here are some example test cases to demonstrate the functionality of the SumSquares function:

Test case 1:
Input: lst = [1, 2, 3]
Expected Output: 14

Test case 2: