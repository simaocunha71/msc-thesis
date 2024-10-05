  return arr.sort((a, b) => {
    const bitCountA = bin(a).split('').filter(x => x === '1').length;
    const bitCountB = bin(b).split('').filter(x => x === '1').length;
    return bitCountA - bitCountB || a - b;
  });

  function bin(num) {
    let result = [];
    while (num > 0) {
      result.push(num % 2);
      num = Math.floor(num / 2);
    }
    return result.reverse().join('');
  }



Explanation:
This is a simple sorting algorithm, it uses the built-in Array.sort method.

The Array.sort method sorts the array based on the return value of the provided compare function. If the compare function returns a negative value, a will be sorted before b. If the compare function returns a positive value, a will be sorted after b. If the compare function returns 0, the relative order of a and b will not change.

The compare function in this solution first counts the number of '1' bits in the binary representation of each number. This is done by converting the number to binary (as a string), splitting the binary string into an array of digits, and then counting the number of '1' digits. For example, 17 is represented as '10001' in binary, so its bitCount is 3.

If the bitCounts of two numbers are the same, the compare function falls back to comparing the numbers directly, in which case the larger number comes first.

In this way, the array is sorted first by the number of '1' bits in the binary representation of each number, and then by the actual decimal value of each number.

*/





































































































