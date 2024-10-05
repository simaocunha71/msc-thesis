  let numStr = num.toString();
  let evenCount = 0;
  let oddCount = 0;
  for (let i = 0; i < numStr.length; i++) {
    if (numStr[i] % 2 === 0) {
      evenCount++;
    } else {
      oddCount++;
    }
  }
  return [evenCount, oddCount];
}

console.log(evenOddCount(-12)); //[1, 1]
console.log(evenOddCount(123)); //[1, 2]
console.log(evenOddCount(11235)); //[2, 3]
console.log(evenOddCount(0)); //[1, 0]
console.log(evenOddCount(1111111)); //[0, 7]
console.log(evenOddCount(2222222)); //[7, 0]
```

This function takes an integer as an argument. It converts the integer to a string, then loops through each character in the string. If the character is divisible by 2 with no remainder, it increments the evenCount variable. Otherwise, it increments the oddCount variable. Finally, it returns an array that contains the count of even and odd digits in the original integer.

The time complexity of this function is O(n), where n is the number of digits in the integer. The space complexity is also O(n), as we are storing the integer as a string.

This function will work for any integer input, including negative integers and zero.

The function will return the count of even and odd digits in the order [evenCount, oddCount]. If there are no even digits, the evenCount will be 0, and if there are no odd digits, the oddCount will be 0.

Here is the function in Python:

```python
def evenOddCount(num):
    numStr = str(abs(num))  # convert to absolute value to handle negative numbers
    evenCount = sum(1 for ch in numStr if int(ch) % 2 == 0)
    oddCount = sum(1 for ch in numStr if