To convert a given number in decimal form to binary format, we can follow the steps below:

1. Initialize an empty string variable called binaryString to store the binary representation of the decimal number.
2. Check if the decimal number is equal to 0. If it is, return the binaryString with all '0' characters.
3. Use a while loop to repeatedly divide the decimal number by 2 and keep track of the remainders.
4. Inside the loop, convert each remainder to a binary representation (either '0' or '1') and append it to the binaryString.
5. After the loop ends, return the binaryString with the binary representation of the decimal number.

Here's a step-by-step explanation of the code provided:

1. Initialize an empty string variable called binaryString.
2. Check if the decimal number is equal to 0. If it is, return the binaryString with all '0' characters.
3. Use a while loop to repeatedly divide the decimal number by 2 and keep track of the remainders.
4. Inside the loop, convert each remainder to a binary representation (either '0' or '1') and append it to the binaryString.
5. After the loop ends, return the binaryString with the binary representation of the decimal number.

For example, if the input decimal number is 15:

- The remainder of 15 divided by 2 is 1, so we append '1' to binaryString.
- The remainder of 7 divided by 2 is 1, so we append '1' to binaryString.
- The remainder of 3 divided by 2 is 1, so we append '1' to binaryString.
- The remainder of 1 divided by 2 is 1, so we append '1' to binaryString.

The resulting binaryString is "db1111db".

*/

function decimalToBinary(decimal) {
  let binaryString = '';
  if (decimal === 0) return binaryString + 'db';
  while (decimal > 0) {
    binaryString = 'db' + (decimal % 2) + binaryString;
    decimal = Math.floor(decimal / 2);
  }
  return binaryString + 'db';
}