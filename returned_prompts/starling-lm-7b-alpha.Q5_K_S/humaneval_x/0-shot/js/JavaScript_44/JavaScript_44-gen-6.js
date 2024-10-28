    const convertToDecimal = (num, base) => {
        let result = 0;
        let power = 1;

        while (num > 0) {
            const digit = num % 10;
            result += digit * power;
            num = Math.floor(num / 10);
            power *= base;
        }
        return result;
    };

    const convertToBase = (num, base) => {
        const result = [];
        while (num > 0) {
            result.push(num % base);
            num = Math.floor(num / base);
        }
        return result.reverse().join('');
    };

    const decimal = convertToDecimal(x, base);
    return convertToBase(decimal, base);
};

changeBase(8, 3); //'22'
changeBase(8, 2); //'1000'
changeBase(7, 2); //'111'

*/

In the given code, the `changeBase` function takes two parameters: `x` (the input number) and `base` (the desired base to convert to). The function first converts the `x` to a decimal number using the `convertToDecimal` function. Then, it converts the decimal number to the desired base using the `convertToBase` function and returns the result as a string.

To test the function, you can use the provided examples. For example, `changeBase(8, 3)` will return the string `'22'`, as it converts the decimal number 8 to base 3. Similarly, `changeBase(8, 2)` will return the string `'1000'`, as it converts the decimal number 8 to base 2. And `changeBase(7, 2)` will return the string `'111'`, as it converts the decimal number 7 to base 2.

Overall, the `changeBase` function provides a convenient way to convert a number from one base to another in JavaScript.

*/

/*

Here is a Python equivalent of the provided JavaScript function:

```python
def change_base(x, base):
    def