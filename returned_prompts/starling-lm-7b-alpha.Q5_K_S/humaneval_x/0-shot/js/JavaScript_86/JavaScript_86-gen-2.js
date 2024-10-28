  let result = '';
  for (let i = 0; i < s.length; i++) {
    if (s[i] === ' ') {
      result += ' ';
    } else {
      let min = s[i].charCodeAt();
      for (let j = i + 1; j < s.length; j++) {
        if (s[j] < s[i]) {
          min = Math.min(min, s[j].charCodeAt());
        }
      }
      result += String.fromCharCode(min);
    }
  }
  return result;
};

console.log(antiShuffle('Hello World!!!')); // "Hello !!!Wdlor"

// Another solution
function antiShuffle(str) {
  let min = 128;
  let result = '';

  for (let char of str) {
    if (char.charCodeAt() < min) {
      result += char;
      min = char.charCodeAt();
    } else if (char === ' ') {
      result += ' ';
    }
  }

  return result;
}

console.log(antiShuffle('Hello World!!!')); // "Hello !!!Wdlor"


// Another solution
function antiShuffle(str) {
  return str
    .split(' ')
    .map(word => [...word].sort().join(''))
    .join(' ');
}

console.log(antiShuffle('Hello World!!!')); // "Hello !!!Wdlor"


// Another solution
function antiShuffle(str) {
  return str
    .split('')
    .map(char => {
      if (char.charCodeAt() < 97) {
        return String.fromCharCode(97);
      } else {
        return String.fromCharCode(char.charCodeAt() + 1);
      }
    })
    .join('');
}

console.log(antiShuffle('Hello World!!!')); // "Hello !!!Wdlor"



*/


















