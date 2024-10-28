  const vowels = 'aeiou';
  let count = 0;

  for (let i = 0; i < s.length; i++) {
    if (vowels.includes(s[i])) {
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
console.log(vowelsCount("rhythm")); // 1
console.log(vowelsCount("apple")); // 2
console.log(vowelsCount("Rhythm")); // 1

This function works by iterating through the given string, and for each character,
it checks if it is a vowel by using the String.prototype.includes method. If it is,
it increments the count. After that, if the last character of the string is 'y',
it increments the count. Finally, it returns the count.
*/


// This function takes a string as input and returns the number of vowels in the string.
const vowelsCount = (s) => {
  const vowels = 'aeiou';
  let count = 0;

  for (let i = 0; i < s.length; i++) {
    if (vowels.includes(s[i])) {
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
console.log(vowelsCount("rhythm")); // 1
console.log(vowelsCount("apple")); // 2
console.log(vowelsCount("Rhythm")); // 1

/*
This function works by iterating through the given string, and for each character,
it checks if it is a vowel by using the String.prototype.includes method. If it is