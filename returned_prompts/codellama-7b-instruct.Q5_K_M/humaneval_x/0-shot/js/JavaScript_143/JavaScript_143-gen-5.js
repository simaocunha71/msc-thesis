/*
  First we split the string into an array of words,
  then we filter the array to contain only words that are prime numbers,
  and finally we join the filtered array into a string
  and return it.
*/
const words = sentence.split(' ');
const primeWords = words.filter((word) => {
  for (let i = 2; i < word.length; i++) {
    if (word % i === 0) return false;
  }
  return true;
});
return primeWords.join(' ');
};
