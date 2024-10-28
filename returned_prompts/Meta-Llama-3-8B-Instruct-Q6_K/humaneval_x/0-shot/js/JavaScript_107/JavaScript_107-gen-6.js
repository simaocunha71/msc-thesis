```javascript
function evenOddPalindrome(n) {
  let evenCount = 0;
  let oddCount = 0;

  for (let i = 1; i <= n; i++) {
    let str = i.toString();
    let isPalindrome = true;

    for (let j = 0; j < str.length / 2; j++) {
      if (str[j] !== str[str.length - 1 - j]) {
        isPalindrome = false;
        break;
      }
    }

    if (isPalindrome && i % 2 === 0) {
      evenCount++;
    } else if (isPalindrome && i % 2 !== 0) {
      oddCount++;
    }
  }

  return [evenCount, oddCount];
}

console.log(evenOddPalindrome(3)); // Output: [1, 2]
console.log(evenOddPalindrome(12)); // Output: [4, 6]
```



This solution uses a simple loop to iterate through all numbers from 1 to `n`. For each number, it converts it to a string and checks if it's a palindrome by comparing the first half of the string with the second half. If it's a palindrome and it's even, it increments the `evenCount` variable; if it's a palindrome and it's odd, it increments the `oddCount` variable. Finally, it returns an array with the counts of even and odd palindromes. The time complexity is O(n), where n is the input number. The space complexity is O(1), as it only uses a constant amount of space.