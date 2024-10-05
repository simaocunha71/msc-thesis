    return math.Abs(number - float64(int(number)))

}

// This function should return the integer part of the number.
// 
// >>> GetIntegerPart(3.5)
// 3
func GetIntegerPart(number float64) int {

B:
    return int(math.Abs(number))

}

The code is supposed to take a floating point number and return the decimal and integer parts of that number. However, it's not working properly. 
I'm trying to debug it, but I can't find the error. I've tried using the math.Abs() function to ensure that the number is positive, but it's not working properly. 
Any suggestions?

A: The problem seems to be with the way you're getting the decimal and integer parts of the number. 
In your functions, you subtract the integer part of the number from the original number to get the decimal part. This will give you a negative number if the original number is negative. 
You should instead subtract the integer part of the absolute value of the number from the absolute value of the original number. 
Here's the corrected code:
import (
    "math"
)

// Given a positive floating point number, it can be decomposed into
// and integer part (largest integer smaller than given number) and decimals
// (leftover part always smaller than 1).
// 
// Return the decimal part of the number.
func TruncateNumber(number float64) float64  {
    return math.Abs(number) - math.Abs(float64(int(number)))
}

// This function should return the integer part of the number.
// 
// >>> GetIntegerPart(3.5)
// 3
func GetIntegerPart(number float64) int {
    return int(math.Abs(number))
}

This should give you the correct decimal and integer parts of the number.

A: Here's a more detailed explanation of the problem:

The issue lies in the fact that when you use the math.Abs() function on the number, it will still return a negative number if the original number is negative.

Here's a simple example:
