    let result = '';
    let aIndex = 0;
    let bIndex = 0;

    while (a.length > aIndex && b.length > bIndex) {
        if (a[aIndex] === b[bIndex]) {
            result += '0';
        } else {
            result += '1';
        }
        aIndex++;
        bIndex++;
    }

    while (a.length > aIndex) {
        result += a[aIndex];
        aIndex++;
    }

    while (b.length > bIndex) {
        result += b[bIndex];
        bIndex++;
    }

    return result;
};

console.log(stringXor('010', '110'));






/* Here are some test cases for your solution:
  >>> stringXor('010', '110')
  '100'
  >>> stringXor('11001', '10101')
  '01100'
  >>> stringXor('10000', '01010')
  '11010'
  >>> stringXor('00000', '11111')
  '11111'

  Your function should return a string that is the binary XOR of the input strings a and b.
  The input strings a and b are guaranteed to be of equal length.
  The binary XOR of two strings is the character-wise XOR of the corresponding characters in the strings.

  Here are some tips:
  - The XOR operator in Python is '^'.
  - The XOR of two 0s is 0, and the XOR of two 1s is 0.
  - You can use the '+' operator to concatenate strings.
  */








































































