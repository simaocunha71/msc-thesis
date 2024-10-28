
Here is my version of the code, with some minor improvements:

In HasCloseElements you should use var distance float64 = math.Abs(numbers[i] - numbers[j]) instead of var distance float64 = math.Abs(numbers[i] - numbers[j]) since you don't need to assign the value to a new variable.
In SeparateParenGroups you can use a buffer instead of a slice to store the current string. This is more efficient since you don't need to allocate a new slice every time you append a character.
In TruncateNumber you can use the math.Trunc function instead of math.Mod to truncate the number. This is more efficient since you don't need to convert the number to a float64 first.
In CheckDictCase you can use a single loop to check if all keys are either in lower case or in upper case. You don't need to check the first key separately. You can use the strings.ToLower function to convert the key to lower case and compare it to the original key. If they are equal, all keys are in lower case. If they are not equal, all keys are in upper case.

Here is the updated code:

import (
    "math"
    "strings"
)

// Check if in given list of numbers, are any two numbers closer to each other than given threshold.
// >>> HasCloseElements([]float64{1.0, 2.0, 3.0}, 0.5)
// false
// >>> HasCloseElements([]float64{1.0, 2.8, 3.0, 4.0, 5.0, 2.0}, 0.3)
// true
func HasCloseElements(numbers []float64, threshold float64) bool {
    for i := 0; i < len(numbers); i++ {
        for j := i + 1; j < len(numbers); j++ {
            if math.Abs(numbers[i] - numbers[j]) < threshold {
                return true
            }
        }
    }
    return false
}

// Input to this