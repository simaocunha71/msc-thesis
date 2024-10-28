To convert a number from one base to another, you can use the following steps:

1. Convert the number to base 10 (decimal).
2. Convert the base 10 number to the target base.

Here's a step-by-step explanation of how the function `changeBase` works:

1. The function `changeBase` takes two arguments: `x` (the number you want to convert) and `base` (the target base).
2. It first converts the input number `x` to base 10 using the `parseInt` function with a radix of `base`. This will give you a decimal representation of the number.
3. Then, it uses a `while` loop to convert the decimal number to the target base. It initializes a variable `result` to an empty string, and a variable `remainder` to 0.
4. Inside the loop, it divides the decimal number by the target base and assigns the remainder to `remainder`.
5. It appends the remainder (as a string) to the `result` string.
6. It updates the decimal number by dividing it by the target base and discarding the remainder.
7. It continues this process until the decimal number becomes 0.
8. Finally, it returns the `result` string, which is the representation of the input number in the target base.

You can test the function with the provided test cases or use your own input.

Note: Make sure the `base` argument is a valid base number (less than 10). Otherwise, the function may not work correctly.

*/

const changeBase = (x, base) => {
  const dec = parseInt(x, base);
  let result = '';

  while (dec > 0) {
    result = (dec % base) + result;
    dec = Math.floor(dec / base);
  }

  return result;
};

console.log(changeBase(8, 3)); // '22'
console.log(changeBase(8, 2)); // '1000'
console.log(changeBase(7, 2)); // '111'



















