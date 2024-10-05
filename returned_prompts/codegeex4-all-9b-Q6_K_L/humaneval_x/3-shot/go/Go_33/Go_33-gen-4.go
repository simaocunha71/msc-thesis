    return math.Mod(number,1)
}

The problem is that the return value of the function is incorrect. The function is supposed to return the decimal part of the number, but it is returning the remainder of the number when divided by 1. This is not the same thing as the decimal part of the number.
For example, if the input number is 3.5, the decimal part of the number is 0.5, but the function is returning 0.0 because 3.5 % 1 is 0.0.
The correct code should be:
func TruncateNumber(number float64) float64 {
    return number - math.Floor(number)
}

This code subtracts the integer part of the number from the original number to get the decimal part.