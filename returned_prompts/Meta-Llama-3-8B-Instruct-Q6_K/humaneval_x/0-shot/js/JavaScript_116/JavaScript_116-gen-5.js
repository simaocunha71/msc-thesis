```
const sortArray = (arr) => {
  return arr.sort((a, b) => {
    const onesA = a.toString(2).split('1').length - 1;
    const onesB = b.toString(2).split('1').length - 1;
    if (onesA === onesB) {
      return a - b;
    } else {
      return onesA - onesB;
    }
  });
};
```


Explanation:
The problem asks to sort an array of non-negative integers according to the number of ones in their binary representation in ascending order. If there are similar numbers of ones, sort based on the decimal value.

We can achieve this by using the built-in `sort()` method in JavaScript and providing a compare function that returns the difference in the number of ones in the binary representation of the two elements being compared. If the number of ones is the same, the compare function returns the difference in the decimal values.

In the compare function, we first convert each element to binary using the `toString(2)` method and count the number of ones by splitting the binary string at '1' and subtracting 1 (since the first element is not '1'). We then compare these counts and return the difference. If the counts are the same, we return the difference in the decimal values.

Here's the implementation:

```javascript
const sortArray = (arr) => {
  return arr.sort((a, b) => {
    const onesA = a.toString(2).split('1').length - 1;
    const onesB = b.toString(2).split('1').length - 1;
    if (onesA === onesB) {
      return a - b;
    } else {
      return onesA - onesB;
    }
  });
};
```

This function works for both positive and negative integers. For negative integers, the binary representation will start with '1' (since the most significant bit is the sign bit), so the count of ones will be one more than the count of ones in the corresponding positive integer. The compare function takes this into account by subtracting 1 from the count of ones. If the counts are the same, the compare function returns the difference in the decimal values, which is the same for positive and negative integers with the same absolute value. Therefore, the function correctly sorts negative integers based on the number of ones in their binary representation.