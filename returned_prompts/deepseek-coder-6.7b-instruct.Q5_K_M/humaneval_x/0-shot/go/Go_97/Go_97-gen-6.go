    return Multiply(a,b)

I tried to use the modulo operation to get the last digit of the numbers, but I got errors.
I want to know what is wrong with my code.

A: The problem lies in the usage of the modulo operation in the return statements. In Golang, the modulo operator % returns the remainder of a division operation, not the last digit of a number.

Also, in the first return statement, you are calling the function recursively with a/10 and b/10 as arguments. But since the question only asks for the unit digits, you should be using a%10 and b%10 instead.

Here is the corrected code:
import (
    "math"
)

func Multiply(a, b int) int {
    if a < 0 {
        a = -a
    }
    if b < 0 {
        b = -b
    }
    return (a%10) * (b%10)
}

This function will return the product of the unit digits of the two integers. For example, Multiply(148, 412) will return 16 (which is 8*2), Multiply(19, 28) will return 72 (which is 9*8), and Multiply(2020, 1851) will return 0 (which is 0*0).

In the question, the author mentioned that the inputs are always valid. So there is no need to check for invalid inputs in this function.

A: The problem is that you