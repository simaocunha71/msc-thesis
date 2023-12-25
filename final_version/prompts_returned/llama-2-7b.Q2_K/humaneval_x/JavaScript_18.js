/* Find how many times a given substring can be found in the original string. Count overlaping cases.
  >>> howManyTimes('', 'a')
  0
  >>> howManyTimes('aaa', 'a')
  3
  >>> howManyTimes('aaaa', 'aa')
  3
  */
const howManyTimes = (string, substring) => {
  let n = string.length;
  for (let j = string.length - substring.length + 1; j <= n; j++)
    if (string.substr(j-substring.length+1, substring.length) == substring) {
      n--;
    }
  return n;
}
