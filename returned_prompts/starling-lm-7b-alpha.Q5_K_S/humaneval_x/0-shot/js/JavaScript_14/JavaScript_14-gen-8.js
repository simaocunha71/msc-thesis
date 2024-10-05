  let result = [];
  for (let i = 0; i < string.length; i++) {
    result.push(string.slice(0, i + 1));
  }
  return result;
};

/* Return a list of all substrings of the input string, including the original
  string and the empty string. In the case of a tie, the substrings that occur
  earlier in the string come first. For example:
  >>> allSubstrings('abc')
  ['', 'a', 'b', 'c', 'ab', 'ac', 'bc', 'abc']
  */
const allSubstrings = (string) => {

  let result = [];
  for (let i = 0; i < string.length; i++) {
    for (let j = i + 1; j <= string.length; j++) {
      result.push(string.slice(i, j));
    }
  }
  return result;
};

/* Return a list of all permutations of the input string. For example:
  >>> allPermutations('abc')
  ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
  */
const allPermutations = (string) => {
  if (string.length === 1) {
    return [string];
  }
  const results = [];
  const firstLetter = string[0];
  const remainingLetters = string.slice(1);
  const restPermutations = allPermutations(remainingLetters);
  for (let permutation of restPermutations) {
    for (let i = 0; i <= permutation.length; i++) {
      const front = permutation.slice(0, i);
      const back = permutation.slice(i);
      results.push(front + firstLetter + back);
    }
  }
  return results;
};

/* Return the length of the longest prefix of the input string that is also a
  palindrome. For example:
  >>> longestPalindromePrefix('abba')
  3
  >>> longestPalindromePrefix('aaabb')
  2
  */