    let result = '';
    while (x > 0) {
        result += String.fromCharCode(x % base + 48);
        x = Math.floor(x / base);
    }
    return result.split('').reverse().join('');
};

changeBase(8, 3) // '22'
changeBase(8, 2) // '1000'
changeBase(7, 2) // '111'

*/

To convert a number from one base to another, follow these steps:

1. Initialize a variable called result to store the final result as an empty string.
2. While the input number x is greater than 0, perform the following steps:
   a. Use the modulus operator (%) to get the remainder of the division of x by the desired base. Add 48 to the remainder to convert the digit to its ASCII value (the ASCII value of '0' is 48, '1' is 49, and so on). Convert the resulting ASCII value to a character using the String.fromCharCode() method, and append it to the result string.
   b. Divide x by the desired base using the Math.floor() function to get the quotient. This step is necessary to move on to the next digit in the number's representation.
3. Return the reversed result string using the split(), reverse(), and join() methods.

By following these steps, the function changeBase() can convert a number from one base to another and return a string representation of the result.

The provided code demonstrates the usage of the changeBase() function with different input values. For example, changeBase(8, 3) returns the string '22' when the base is 3, and changeBase(7, 2) returns the string '111' when the base is 2.

You can test the function by calling it with different input values to convert numbers from one base to another.

*/


// 