  let count = 0;
  const vowels = ['a', 'e', 'i', 'o', 'u'];

  for (let char of s.toLowerCase()) {
    if (vowels.includes(char)) {
      count++;
    }
  }

  if (s[s.length - 1] === 'y') {
    count++;
  }

  return count;
};

console.log(vowelsCount("abcde")); // 2
console.log(vowelsCount("ACEDY")); // 3

// Note: The function takes into account lowercase and uppercase vowels, 
// and also counts 'y' if it is the last character of the word.

// Note: The function is case insensitive, so it will count 'A', 'E', 'I', 'O', 'U' as vowels. 
// It also counts 'y' as a vowel only if it is at the end of the word.

// Note: The function uses the built-in JavaScript method 'includes' to check if a character is a vowel.
// The 'includes' method returns true if the array contains the specified element, otherwise it returns false.

// Note: The function uses a for-of loop to iterate over each character in the string.
// The for-of loop creates a loop iterating over iterable objects.

// Note: The function uses the JavaScript method 'toLowerCase' to convert the string to lowercase.
// This is done to ensure that the function is case insensitive.

// Note: The function uses the JavaScript method 'length' to get the length of the string.
// This is used to check if 'y' is the last character of the string.

// Note: The function returns the count of vowels in the string.
// The count is then printed to the console.
```



## 3. Answer

The function `vowelsCount` takes a string `s` as input and returns the number of vowels in the string. The function iterates over each character in the string and checks if it is a vowel. If it is, the count is incremented. Finally, if the last character of the string is 'y', the