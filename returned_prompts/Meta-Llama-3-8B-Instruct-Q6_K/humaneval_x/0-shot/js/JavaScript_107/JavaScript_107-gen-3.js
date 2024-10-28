```
const evenOddPalindrome = (n) => {
  let evenCount = 0;
  let oddCount = 0;

  for (let i = 1; i <= n; i++) {
    const str = i.toString();
    if (str === str.split('').reverse().join('')) {
      if (i % 2 === 0) {
        evenCount++;
      } else {
        oddCount++;
      }
    }
  }

  return [evenCount, oddCount];
};
```


Explanation:
We iterate through all the numbers from 1 to n, and for each number, we check if it's a palindrome. If it is, we check if it's even or odd. We increment the corresponding count variable. Finally, we return the counts as a list. The time complexity is O(n) as we iterate through all numbers, and the space complexity is O(1) as we only use a constant amount of space.