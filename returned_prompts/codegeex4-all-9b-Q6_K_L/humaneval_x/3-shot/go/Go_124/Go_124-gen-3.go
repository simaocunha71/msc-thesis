
There's a lot of code in these 4 functions, but it's mostly straightforward.  I'd like to suggest a few changes that would improve the readability and maintainability of your code:

1.  Don't use magic numbers.  Replace 0.5, 0.3, and 1 with named constants.
2.  Use for range loops whenever possible.  They're more concise and less error-prone than traditional for loops.
3.  Use switch statements to handle cases where there are multiple possible outcomes.
4.  Use defer statements to handle cleanup tasks, such as closing files or releasing resources.
5.  Use error handling to handle potential errors, such as invalid input or file not found.
6.  Use comments to explain complex logic or code that's not immediately obvious.
7.  Use meaningful names for variables and functions.  This makes the code easier to understand and maintain.
8.  Use consistent formatting and style throughout the code.  This makes it easier to read and understand.

Here's an updated version of your code with these suggestions:

package main

import (
    "fmt"
    "math"
    "strconv"
    "strings"
)

const (
    threshold1 = 0.5
    threshold2 = 0.3
)

func HasCloseElements(numbers []float64, threshold float64) bool {
    for _, num1 := range numbers {
        for _, num2 := range numbers {
           