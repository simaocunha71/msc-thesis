  const isPalindrome = (num) => {
    let str = String(num);
    let len = str.length;
    for (let i = 0; i < Math.floor(len / 2); i++) {
      if (str[i] !== str[len - 1 - i]) {
        return false;
      }
    }
    return true;
  }

  let evenCount = 0, oddCount = 0;
  for (let i = 1; i <= n; i++) {
    if (isPalindrome(i)) {
      if (i % 2 === 0) {
        evenCount++;
      } else {
        oddCount++;
      }
    }
  }
  return [evenCount, oddCount];
}
evenOddPalindrome(3);
evenOddPalindrome(12);
```

### Explanation

We need to count the number of integer palindromes between 1 and n, and we also need to categorize them into even and odd.

So we create a function `isPalindrome` that checks if a number is palindrome or not. Then we iterate from 1 to n, and for each number, we check if it's palindrome or not. If it's palindrome, we then check if it's even or odd and increment the corresponding count.

Finally, we return the counts in an array.

### Complexity Analysis

- Time complexity: O(n^2) because in the worst case, we have to check n numbers and for each number, we are doing a palindrome check which takes O(n) time.
- Space complexity: O(1) because we are using constant space. We are not using any data structure that scales with the input size.

### Test Cases

```javascript
console.log(evenOddPalindrome(3)); // [1, 2]
console.log(evenOddPalindrome(12)); // [4, 6]
```

This function should pass these test cases.

---

## Question 2

### Problem

