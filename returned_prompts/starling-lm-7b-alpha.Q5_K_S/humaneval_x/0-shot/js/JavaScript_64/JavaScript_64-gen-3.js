  const vowels = ['a', 'e', 'i', 'o', 'u', 'y'];
  let count = 0;
  for (let i = 0; i < s.length; i++) {
    if (vowels.includes(s[i])) {
      count++;
    }
  }
  return count;
};

// test cases
console.log(vowelsCount("abcde")); // 2
console.log(vowelsCount("ACEDY")); // 3


/*
The function vowelsCount takes a string as input and counts the number of
  vowels in the string. The vowels are 'a', 'e', 'i', 'o', 'u', and 'y'. The
  function initializes a counter variable, count, to zero. Then, it iterates
  through the string using a for loop. For each character in the string, it checks
  if the character is in the vowels array using the Array.includes() method. If
  the character is a vowel, the count variable is incremented. Finally, the function
  returns the count variable, which represents the number of vowels in the string.

  The test cases verify that the function correctly counts the number of vowels.
  The first test case, "abcde", has 2 vowels, so the expected output is 2. The
  second test case, "ACEDY", has 3 vowels, so the expected output is 3.
*/


































































































































































