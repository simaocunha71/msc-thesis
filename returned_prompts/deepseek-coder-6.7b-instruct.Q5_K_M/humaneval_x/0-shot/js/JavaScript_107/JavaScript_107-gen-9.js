  const isPalindrome = (num) => {
    const str = num.toString();
    const len = str.length;
    for(let i = 0; i < len/2; i++) {
      if(str[i] !== str[len - 1 - i]) return false;
    }
    return true;
  }

  let even = 0, odd = 0;
  for(let i = 1; i <= n; i++) {
    if(isPalindrome(i)) {
      if(i % 2 === 0) even++;
      else odd++;
    }
  }

  return [even, odd];
}

console.log(evenOddPalindrome(3)); // [1, 2]
console.log(evenOddPalindrome(12)); // [4, 6]
```
This program works by first defining a helper function `isPalindrome` that checks if a number is a palindrome or not. The function `evenOddPalindrome` then iterates through all numbers from 1 to `n`, checks if each number is a palindrome, and increments the appropriate counter if the number is even or odd. Finally, the function returns a list with the number of even and odd palindromes.

Please note that this solution has a time complexity of O(n^2), as for each number, we are checking if it is a palindrome which itself takes O(n) time. So, the overall time complexity is O(n^2). This is because the function `evenOddPalindrome` is called for each number from 1 to `n`, and for each call, we are checking if the number is a palindrome.

However, this solution can be optimized to O(n) by pre-calculating all palindromes in the range [1, 10^6] (where 10^6 is the maximum possible value of `n`). This can be done by generating all palindromes and storing them in a set. Then, for each number `i` from 1 to `n`, we can check if `i` is in the set of palindromes. This would reduce the time complexity to O