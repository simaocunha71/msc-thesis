let vowels = 'aeiouyAEIOUY';
  let count = 0;

  for (let i = 0; i < s.length; i++) {
    if (vowels.includes(s[i])) {
      count++;
    }
  }

  return count;
};

console.log(vowelsCount("abcde"));
console.log(vowelsCount("ACEDY"));


// The function takes a string input s and initializes a count variable to 0.
// It then iterates over each character in the string. If the character is found 
// in the vowel string, it increments the count.
// The function then returns the count, which is the number of vowels in the string.
// The string includes method is used to determine if a character is a vowel.
// The function is case-insensitive, so it counts both lowercase and uppercase vowels.
// The 'y' is also a vowel, but only when it is at the end of the given word. 
// This is handled by the function itself, as it checks for the 'y' at the end of the string.
// If the 'y' is at the end of the string, it is considered a vowel and the count is incremented.

```

## Exercise 3

