```
const evenOddPalindrome = (n) => {
  let evenCount = 0;
  let oddCount = 0;

  for (let i = 1; i <= n; i++) {
    let str = i.toString();
    let isPalindrome = true;
    let left = 0;
    let right = str.length - 1;

    while (left < right) {
      if (str[left] !== str[right]) {
        isPalindrome = false;
        break;
      }
      left++;
      right--;
    }

    if (isPalindrome && i % 2 === 0) {
      evenCount++;
    } else if (isPalindrome && i % 2 !== 0) {
      oddCount++;
    }
  }

  return [evenCount, oddCount];
};
```


Explanation:

1. Initialize two counters, `evenCount` and `oddCount`, to keep track of the number of even and odd integer palindromes respectively.

2. Iterate through the range of numbers from 1 to `n`.

3. For each number, convert it to a string and check if it's a palindrome. A palindrome is a number or a string that reads the same backward as forward.

4. If the number is a palindrome and it's even, increment `evenCount`. If the number is a palindrome and it's odd, increment `oddCount`.

5. Finally, return an array with the counts of even and odd integer palindromes.

This solution has a time complexity of O(n), where n is the input number. This is because we iterate through the range of numbers from 1 to `n`. The space complexity is O(1), as we use a constant amount of space to store the counters and other variables.