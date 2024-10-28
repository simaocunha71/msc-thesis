  return s.split(' ').map(word => {
    return word.split('').sort((a, b) => a.charCodeAt(0) - b.charCodeAt(0)).join('');
  }).join(' ');

};

console.log(antiShuffle('Hi')); // 'Hi'
console.log(antiShuffle('hello')); // 'ehllo'
console.log(antiShuffle('Hello World!!!')); // 'Hello  !!!Wdlor'

*/

const antiShuffle = (s) => {
  return s.split(' ').map(word => {
    return word.split('').sort((a, b) => a.charCodeAt(0) - b.charCodeAt(0)).join('');
  }).join(' ');
};

console.log(antiShuffle('Hi')); // 'Hi'
console.log(antiShuffle('hello')); // 'ehllo'
console.log(antiShuffle('Hello World!!!')); // 'Hello  !!!Wdlor'

// solution 2:

const antiShuffle2 = (s) => {
  return s.split('').sort((a, b) => a.charCodeAt(0) - b.charCodeAt(0)).join('');
};

console.log(antiShuffle2('Hi')); // 'Hi'
console.log(antiShuffle2('hello')); // 'ehllo'
console.log(antiShuffle2('Hello World!!!')); // ' !!!HWdelor'

// solution 3:

const antiShuffle3 = (s) => {
  return s.split('').sort((a, b) => a.localeCompare(b)).join('');
};

console.log(antiShuffle3('Hi')); // 'Hi'
console.log(antiShuffle3('hello')); // 'ehllo'
console.log(antiShuffle3('Hello World!!!')); // ' !!!HWdelor'

// solution 4:

const antiShuffle4 = (s) => {
  return [...s].sort((a, b) => a.localeCompare(b)).join('');
};
