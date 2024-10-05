```
const stringXor = (a, b) => {
  let result = '';
  let carry = 0;
  let i = a.length - 1;
  let j = b.length - 1;

  while (i >= 0 || j >= 0 || carry) {
    let bitA = i >= 0 ? parseInt(a[i--]) : 0;
    let bitB = j >= 0 ? parseInt(b[j--]) : 0;
    let sum = bitA ^ bitB ^ carry;
    carry = (sum & 1) ? 1 : 0;
    result = (sum % 2) + result;
  }
  return result;
};
```


Explanation:
The function stringXor takes two strings a and b as inputs. It performs binary XOR operation on these strings and returns the result as a string.

We initialize an empty string result to store the result, and carry variable to keep track of the carry bit.

We then iterate over the strings a and b from right to left (from the last character to the first). We convert each character to an integer using parseInt() and store it in bitA and bitB. We perform XOR operation on these two bits and the carry bit to get the sum.

We update the carry bit if the sum is odd (i.e., 1), and update the result by prepending the least significant bit of the sum to the result.

Finally, we return the result string. If the carry bit is still 1 after the loop, we need to add it to the result string. This is because the XOR operation does not propagate the carry bit to the next iteration.

This solution has a time complexity of O(n), where n is the length of the input strings, and a space complexity of O(n), where n is the length of the output string. This is because we are iterating over the input strings and storing the result in a string.