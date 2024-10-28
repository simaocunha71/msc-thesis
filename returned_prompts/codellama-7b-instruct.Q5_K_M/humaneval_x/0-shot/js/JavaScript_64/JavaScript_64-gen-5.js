/*Write a function countVowels which takes a string representing
  a word as input and returns the number of vowels in the string.
  Vowels in this case are 'a', 'e', 'i', 'o', 'u'. Here, 'y' is also a
  vowel, but only when it is at the end of the given word.

  Example:
  >>> countVowels("abcde")
  2
  >>> countVowels("ACEDY")
  3
  */
  const countVowels = (word) => {
    let count = 0;
    for (let i = 0; i < word.length; i++) {
      if (word[i] === 'a' || word[i] === 'e' || word[i] === 'i' || word[i] === 'o' || word[i] === 'u') {
        count++;
      }
      if (word[i] === 'y' && i === word.length - 1) {
        count++;
      }
    }
    return count;
  };

  console.log(countVowels("abcde")); // 2
  console.log(countVowels("ACEDY")); // 3
  console.log(countVowels("aeiou")); // 5
  console.log(countVowels("aeiouy")); // 6
  console.log(countVowels("aeiouyc")); // 7

  B:
  /*Write a function countVowels which takes a string representing
  a word as input and returns the number of vowels in the string.
  Vowels in this case are 'a', 'e', 'i', 'o', 'u'. Here, 'y' is also a
  vowel, but only when it is at the end of the given word.

  Example:
  >>> countVowels("abcde")
  2
  >>> countVowels("ACEDY")
  3
  */
  const countVowels = (word) => {
    const vowels = ['a', 'e', 'i', 'o', 'u', 'y'];
   