/* Find how many times a given substring can be found in the original string. Count overlaping cases.
  >>> howManyTimes('', 'a')
  0
  >>> howManyTimes('aaa', 'a')
  3
  >>> howManyTimes('aaaa', 'aa')
  3
  */
const howManyTimes = (string, substring) => {
  let count = 0;
  if (string.length < substring.length) {
    return count;
  }
  for (let i = 0; i < string.length - substring.length; i++) {
    if (string.substring(i, i + substring.length) === substring) {
      count++;
      i += substring.length - 1;
    }
  }
  return count;
};

