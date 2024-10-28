    return number - math.Floor(number)
    // Alternatively, you can use the modulo operator (%)
    // return number % 1
}

In this function, why is math.Floor(number) used instead of math.Ceil(number)?

Why is number - math.Floor(number) used instead of math.Mod(number, 1)?

Why is number % 1 used instead of math.Mod(number, 1)?

Answer:

The reason why the modulo operator (%) is used instead of math.Mod() is because the modulo operator is simpler to understand and it is more efficient.

The reason why math.Floor(number) is used instead of math.Ceil(number) is because the math.Floor(number) function returns the largest integer less than or equal to the given number, while math.Ceil(number) returns the smallest integer greater than or equal to the given number. Since we want to obtain the decimal part of the number, we need to use math.Floor(number) instead of math.Ceil(number).

The reason why number - math.Floor(number) is used instead of math.Mod(number, 1) is because math.Mod(number, 1) returns the remainder of the division of the number by 1, while number - math.Floor(number) subtracts the largest integer less than or equal to the number from the number itself. Since we want to obtain the decimal part of the number, we need to use number - math.Floor(number) instead of math.Mod(number, 1).

The reason why number % 1 is used instead of math.Mod(number, 1) is because number % 1 is the modulo operator for the number and 1, while math.Mod(number, 1) is the modulo function for the number and 1. Since the modulo operator is simpler to understand and it is more efficient, we use number % 1 instead of math.Mod(number, 1).

Here are some additional resources that you may find helpful:

- [Modulo Operator](https://en.wikipedia.org/wiki/Modulo_operation)
- [Modulo Function](https://en.wikipedia.org/wiki