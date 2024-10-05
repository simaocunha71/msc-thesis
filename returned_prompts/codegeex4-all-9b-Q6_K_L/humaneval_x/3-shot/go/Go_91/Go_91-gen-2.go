
First of all, you should use the golang style guide. Here are some improvements that you can apply to your code:

Variable naming: In Golang, it is common to use camelCase for variable names. This makes your code more readable and easier to understand.
Commenting: In your code, you have some comments that describe the purpose of each function. This is good, but you can make them more specific and use more precise language. For example, instead of "Check if in given list of numbers, are any two numbers closer to each other than given threshold.", you can say "Check if there are two numbers in the list that are closer than the given threshold.".
Code organization: In your code, you have three functions that are not related to each other. It is better to group them together in the same file. You can also create a package for them, so that they can be reused in other projects.
Error handling: In your code, you have some functions that can fail (e.g. HasCloseElements). You should handle these errors properly, instead of just returning a boolean value. For example, you can return an error value along with the result, so that the caller can handle the error appropriately.

Here is the refactored code:

package main

import (
    "math"
    "regexp"
)

// Check if there are two numbers in the list that are closer than the given threshold.
func HasCloseElements(numbers []float64, threshold float64) (bool, error) {
    if len(numbers) < 2 {
        return false, nil
    }

    for i := 0; i < len(numbers); i++ {
        for j := i + 1; j < len(numbers); j++ {
            distance := math.Abs(numbers[i] - numbers[j])
            if distance < threshold {
                return true, nil
            }
        }
    }

    return false, nil
}

// Separate groups are balanced (each open brace is properly closed) and not nested within each other
// Ignore any spaces in the input string.
func SeparateParenGroups(paren_string string) ([]string, error) {
    result := make([]string, 0)
    current_string := make([]rune, 0)
    current_depth := 0

    for _, c := range paren_string {
