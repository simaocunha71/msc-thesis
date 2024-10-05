```
function changeBase(x, base) {
    let digits = "0123456789";
    let result = "";
    while (x > 0) {
        result = digits[x % base] + result;
        x = Math.floor(x / base);
    }
    return result;
}
```


This function converts a number from one base to another. It uses the remainder of the number when divided by the new base to get the next digit, and then divides the number by the new base to get the next remainder. This process is repeated until the number becomes 0. The digits of the number in the new base are then concatenated together in reverse order to form the final result.

The function takes two parameters, x, the number to be converted, and base, the base to convert it to. It uses a string called digits that contains the digits of the new base, and a variable result to build the final string.

The function then enters a loop where it takes the remainder of x when divided by base, adds it to the result string, and then divides x by base. This process is repeated until x becomes 0.

Finally, the function returns the result string, which is the number in the new base.