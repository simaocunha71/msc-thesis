  // Split the string into words and blank spaces
  let words = s.split(' ');
  let spaces = [];
  for(let i=0; i<s.length; i++) {
    if(s[i] === ' ') {
      spaces.push(i);
    }
  }

  // For each word, sort its characters
  for(let i=0; i<words.length; i++) {
    words[i] = words[i].split('').sort((a, b) => a.charCodeAt(0) - b.charCodeAt(0)).join('');
  }

  // Reconstruct the string with the sorted words and blank spaces
  let result = '';
  let j = 0;
  for(let i=0; i<s.length; i++) {
    if(spaces.includes(i)) {
      result += ' ';
    } else {
      result += words[j][0];
      words[j] = words[j].slice(1);
      if(words[j] === '') j++;
    }
  }

  return result;
}

console.log(antiShuffle('Hi')); // 'Hi'
console.log(antiShuffle('hello')); // 'ehllo'
console.log(antiShuffle('Hello World!!!')); // 'Hello  !!!Wdlor'
console.log(antiShuffle('I am a sentence')); // 'I aa a ceensent'

```




























































































































































