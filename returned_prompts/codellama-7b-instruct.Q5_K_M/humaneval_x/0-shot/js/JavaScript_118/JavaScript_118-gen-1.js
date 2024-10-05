/*
  Solution:
  - split the word into an array of chars
  - check if the first char is a consonant
  - check if the last char is a vowel
  - check each char in the middle and return the first vowel
  - if there is no vowel, return empty string
  */
  const wordArray = word.split('');

  if (wordArray[0].match(/[a-z]/i)) {
    wordArray.shift();
  }

  if (wordArray[wordArray.length - 1].match(/[aeiou]/i)) {
    wordArray.pop();
  }

  for (let i = 0; i < wordArray.length; i++) {
    if (wordArray[i].match(/[aeiou]/i)) {
      return wordArray[i];
    }
  }

  return '';
}


