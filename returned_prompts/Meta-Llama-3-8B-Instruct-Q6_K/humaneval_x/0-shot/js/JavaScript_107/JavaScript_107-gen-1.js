Here is the solution in JavaScript:

```javascript
const evenOddPalindrome = (n) => {
  let even = 0, odd = 0;
  for(let i = 1; i <= n; i++) {
    let str = i.toString();
    let isPalindrome = true;
    let left = 0, right = str.length - 1;
    while(left < right) {
      if(str[left] !== str[right]) {
        isPalindrome = false;
        break;
      }
      left++;
      right--;
    }
    if(isPalindrome) {
      if(i % 2 === 0) even++;
      else odd++;
    }
  }
  return [even, odd];
}
```
The function `evenOddPalindrome` takes an integer `n` as input and returns an array with two elements. The first element is the count of even integer palindromes and the second element is the count of odd integer palindromes in the range [1, n].

The function iterates over the range [1, n] and checks if each integer is a palindrome. If it is a palindrome, it checks if it is even or odd and increments the corresponding counter. Finally, it returns the counts of even and odd palindromes.

The time complexity of this function is O(n), where n is the input integer, because it needs to iterate over the range [1, n] to check for palindromes. The space complexity is O(1), because it only uses a constant amount of space to store the counters and other variables.