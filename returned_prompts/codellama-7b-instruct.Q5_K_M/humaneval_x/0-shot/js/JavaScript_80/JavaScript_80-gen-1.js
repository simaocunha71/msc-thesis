/*
  Check if the string is at least 3 characters long. If not return false.
  Check if the string has any 3 consecutive letters that are not distinct. If so return false.
  If all checks pass return true.
*/
const isHappy = (s) => {
  if (s.length < 3) return false;
  if (s.length % 3 === 0) return s.split('').reduce((acc, curr, i, arr) => {
    if (i % 3 === 0 && curr === arr[i + 1] && curr === arr[i + 2]) return false;
    return acc;
  }, true);
  return true;
}

