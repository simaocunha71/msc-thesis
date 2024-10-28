const isPalindrome = str => str === str.split('').reverse().join('');

const makePalindrome = str => {
  const [postfix, prefix] = str.split(/(\w*?(?=\w*?\1\w*?$))/);
  return str + prefix.split('').reverse().join('');
};

/*
  Test cases
  >>> makePalindrome('catac')
  'catac'
  >>> makePalindrome('cat')
  'catac'
  */

