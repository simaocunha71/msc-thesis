
In HasCloseElements, you are missing a closing parenthesis on the for loop that iterates over the numbers.
In SeparateParenGroups, you are appending closing parentheses to your current_string even when the depth is not zero. This causes the string to be longer than it should be. You should only append closing parentheses when the depth is zero.
In TruncateNumber, you are using the modulo operator to truncate the number. However, the result will be a float64, even if the number is an integer. You should cast the result to an int before returning it.
In FindMax, you are using a map to count the number of unique characters in each word. However, you are not considering the case where the word is an empty string. You should check for this case before calculating the number of unique characters.

Here are the corrected versions of your code:
import (
    "math"
)

// Check if in given list of numbers, are any two numbers closer to each other than given threshold.
// >>> HasCloseElements([]float64{1.0, 2.0, 3.0}, 0.5)
// false
// >>> HasCloseElements([]float64{1.0, 2.8, 3.0, 4.0, 5.0, 2.0}, 0.3)
// true
func HasCloseElements(numbers []float64, threshold float64) bool {
    for i := 0; i < len(numbers); i++ {
        for j := i + 1; j < len(numbers); j++ {
            var distance float64 = math.Abs(numbers[i] - numbers[j])
            if distance < threshold {
                return true
            }
        }
    }
    return false
}

// Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
// separate those group into separate strings and return the list of those.
// Separate groups are balanced (each open brace is properly closed) and not