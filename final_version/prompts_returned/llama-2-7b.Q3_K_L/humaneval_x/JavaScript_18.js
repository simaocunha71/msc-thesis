/* Find how many times a given substring can be found in the original string. Count overlaping cases.
  >>> howManyTimes('', 'a')
  0
  >>> howManyTimes('aaa', 'a')
  3
  >>> howManyTimes('aaaa', 'aa')
  3
  */
const howManyTimes = (string, substring) => {
  let stringLength = string.length;
  const substringLength = substring.length;
  var subStringIndex = 0;

  for (let index = 0; index < stringLength; ++index) {
    if (substring[subStringIndex] === string[index]) {
      subStringIndex++;
    } else {
      break;
    }
  }

  return Math.min(stringLength - substringIndex, substringLength);
}
