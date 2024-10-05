const allPrefixes = (string) => {
  let prefixes = [];
  for (let i = 1; i <= string.length; i++) {
    prefixes.push(string.slice(0, i));
  }
  return prefixes;
};

/* Return the index of the first occurrence of needle in the haystack, or -1 if needle is not part of haystack
  >>> firstOccurrence('abcde', 'b')
  1
  >>> firstOccurrence('abcde', 'f')
  -1
  */
const firstOccurrence = (haystack, needle) => {
  let index = -1;
  for (let i = 0; i < haystack.length; i++) {
    if (haystack[i] === needle[0]) {
      index = i;
      for (let j = 0; j < needle.length; j++) {
        if (haystack[index + j] !== needle[j]) {
          index = -1;
          break;
        }
      }
    }
  }
  return index;
};

/* Return a list of all the substrings from the input string
  >>> allSubstrings('abc')
  [ 'a', 'b', 'c', 'ab', 'bc', 'abc' ]
  */
const allSubstrings = (string) => {
  let substrings = [];
  for (let i = 0; i < string.length; i++) {
    for (let j = i + 1; j <= string.length; j++) {
      substrings.push(string.slice(i, j));
    }
  }
  return substrings;
};

/* Return the index of the last occurrence of needle in the haystack, or -1 if needle is not part of haystack
  >>> lastOccurrence('abcde', 'e')
  4
  >>> lastOccurrence('abcde', 'f')
  -1
  */
const lastOccurrence = (haystack, needle) => {
  let index = -1;
  for (let i = haystack.length - 1; i >= 0; i--) {