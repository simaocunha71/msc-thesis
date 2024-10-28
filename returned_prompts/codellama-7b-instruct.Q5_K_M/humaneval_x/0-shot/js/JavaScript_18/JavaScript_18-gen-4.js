const howManyTimes = (string, substring) => {
  return string.split(substring).length - 1;
}

B:
const howManyTimes = (string, substring) => {
  return string.match(substring).length;
}

C:
const howManyTimes = (string, substring) => {
  return string.split(substring).length - 1;
}

D:
const howManyTimes = (string, substring) => {
  return string.match(substring).length;
}
