const vowelsCount = (word) => {
  let vowels = 0;
  for (let i = 0; i < word.length; i++) {
    if (word[i] === 'a' || word[i] === 'e' || word[i] === 'i' || word[i] === 'o' || word[i] === 'u' || word[i] === 'y') {
      vowels++;
    }
  }
  return vowels;
}

// console.log(vowelsCount('abcde'))

B:
const vowelsCount = (word) => {
  return word.replace(/[^aeiouy]/g, '').length;
}

// console.log(vowelsCount('abcde'))

C:
const vowelsCount = (word) => {
  return word.split('').filter(l => 'aeiouy'.includes(l)).length;
}

// console.log(vowelsCount('abcde'))

D:
const vowelsCount = (word) => {
  return word.replace(/[^aeiouy]/g, '').length;
}

// console.log(vowelsCount('abcde'))

E:
const vowelsCount = (word) => {
  return word.split('').filter(l => 'aeiouy'.includes(l)).length;
}

// console.log(vowelsCount('abcde'))

F:
const vowelsCount = (word) => {
  return word.replace(/[^aeiouy]/g, '').length;
}

// console.log(vowelsCount('abcde'))

G:
const vowelsCount = (word) => {
  return word.split('').filter(l => 'aeiouy'.includes(l)).length;
}

// console.log(vowelsCount('abcde'))

H:
const vowelsCount = (word) => {
  return word.replace(/[^aeiouy]/g, '').length;
}

// console.log(vowelsCount('abcde