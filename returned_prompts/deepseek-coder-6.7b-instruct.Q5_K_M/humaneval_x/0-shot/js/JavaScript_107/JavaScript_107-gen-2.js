  const isPalindrome = (x) => {
    const str = x.toString();
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

console.log(evenOddPalindrome(3)) // [1, 2]
console.log(evenOddPalindrome(12)) // [4, 6]




// Note: The palindrome number is the number that remains the same when its digits are reversed. For example, 121, 12321, 1001 are all palindrome numbers.
// Note: The solution is a JavaScript solution, if you are looking for a solution in a different language, you might have to adjust it a little.

// Note: This solution is a brute-force solution and it has a time complexity of O(n^2). So, it may not be efficient for large inputs.

// Note: This solution uses a helper function isPalindrome that checks whether a given number is a palindrome or not.

// Note: The main function evenOddPalindrome iterates over the range from 1 to n and for each number it checks whether it is a palindrome or not. If it is, it increments the corresponding counter. At the end, it returns a list that has the count of even and odd palindromes.

// Note: The counters are initialized to 0 and then incremented for each palindrome that is found.

// Note: The even and odd palindromes are counted separately.

// Note: The function returns the counts as a list, where the first element is the count of even palindromes and the second element is the count of odd palindromes