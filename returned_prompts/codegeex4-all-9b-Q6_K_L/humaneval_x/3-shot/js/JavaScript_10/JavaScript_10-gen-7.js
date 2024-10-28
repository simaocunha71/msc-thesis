  if (isPalindrome(string)) {
    return string;
  }

  var postfix = string.slice(string.length - 1);
  while (!isPalindrome(postfix)) {
    postfix = postfix.slice(1);
  }

  var prefix = string.slice(0, string.length - postfix.length);
  return string + prefix.split('').reverse().join('');
}

/* Generate all possible permutations of a given string.
  >>> generatePermutations('abc')
  ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
  */
const generatePermutations = (string) => {
  if (string.length < 2) {
    return [string];
  }

  var permutations = [];
  for (const c of string) {
    var remaining = string.split('').filter(x => x != c);
    var remainingPermutations = generatePermutations(remaining.join(''));
    for (const p of remainingPermutations) {
      permutations.push(c + p);
    }
  }

  return permutations;
}

/* Given a string, generate all possible substrings
  >>> generateSubstrings('abc')
  ['a', 'ab', 'abc', 'b', 'bc', 'c']
  */
const generateSubstrings = (string) => {
  var substrings = [];
  for (let i = 0; i < string.length; i++) {
    for (let j = i + 1; j <= string.length; j++) {
      substrings.push(string.slice(i, j));
    }
  }

  return substrings;
}

/* Given a string, generate all possible subwords
  >>> generateSubwords('abc')
  ['a', 'b', 'c', 'ab', 'bc', 'abc']
  */
const generateSubwords = (string) => {
  var subwords = [];
  for (let i = 0; i < string.length; i++) {
    for (let j = i; j <= string.length; j++) {
      subwords.push(string.slice(i, j));
    }
  }

  return subwords;
}

/* Given a string, generate all possible subwords
  >>> generateSubwords('abc')
  ['a', 'b', 'c', 'ab', 'bc', 'abc']
  */
const generateSubwords = (string) => {
  var subwords = [];
  for (let i = 0; i < string.length; i++) {
    for (let j = i; j <=