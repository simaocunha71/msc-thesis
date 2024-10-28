/*
  Solution:
  * Use filter to get the words from the original sentence,
  * Use map to get the length of each word,
  * Use filter again to get the words whose length is prime,
  * Use join to get a string out of an array,
  * Use slice to get the first word of the new string

  O(n) time
  O(n) space
  */
  const words = sentence.split(' ');
  const primeWords = words.filter(word => {
    const wordLength = word.length;
    return wordLength > 1 && [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37].includes(wordLength);
  });

  return primeWords.join(' ').slice(0, primeWords[0].length);
};
