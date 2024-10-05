  let count = 0;
  const vowels = ['a', 'e', 'i', 'o', 'u'];

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
console.log(vowelsCount("AaEiOy")); // 5

*/



// Here is a simpler solution using filter method

const vowelsCount = (s) => {
  const vowels = ['a', 'e', 'i', 'o', 'u'];
  let count = [...s].filter(letter => vowels.includes(letter)).length;
  if (s[s.length - 1] === 'y') {
    count++;
  }
  return count;
};

console.log(vowelsCount("abcde")); // 2
console.log(vowelsCount("ACEDY")); // 3
console.log(vowelsCount("rhythm")); // 1
console.log(vowelsCount("AaEiOy")); // 5

*/


// Here is a more simpler solution using Regular expressions

const vowelsCount = (s) => {
  const matches = s.match(/[aeiou]/gi);
  const count = matches ? matches.length : 0;
  if (s[s.length - 1] === 'y') {
    count++;
  }
  return count;
};

console.log(vowelsCount("abcde")); // 2
console.log(vowelsCount("ACEDY")); // 3
console.log(vowelsCount("rhythm")); // 1
console.log(vowelsCount("AaEiOy"));