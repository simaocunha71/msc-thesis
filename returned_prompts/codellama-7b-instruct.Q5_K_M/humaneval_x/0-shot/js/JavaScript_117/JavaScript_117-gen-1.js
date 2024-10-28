
const selectWords = (s, n) => {
  const words = s.split(' ');
  let result = []
  for (let i = 0; i < words.length; i++) {
    if (countConsonants(words[i]) == n) {
      result.push(words[i])
    }
  }
  return result;
}

function countConsonants(word) {
  let count = 0;
  for (let i = 0; i < word.length; i++) {
    if (isConsonant(word[i])) {
      count++;
    }
  }
  return count;
}

function isConsonant(char) {
  return /[bcdfghjklmnpqrstvwxz]/i.test(char);
}
