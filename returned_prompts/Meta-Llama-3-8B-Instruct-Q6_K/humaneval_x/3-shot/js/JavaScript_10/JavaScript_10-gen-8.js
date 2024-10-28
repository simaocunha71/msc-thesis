  let reverse = string.split('').reverse().join('');
  let i = 0;
  while (i < string.length && string[i] == reverse[i]) {
    i++;
  }
  return string + reverse.substring(i);
}  // https://www.freecodecamp.org/learn/scientific-computing-with-python/coding-challenge:make-palindrome



