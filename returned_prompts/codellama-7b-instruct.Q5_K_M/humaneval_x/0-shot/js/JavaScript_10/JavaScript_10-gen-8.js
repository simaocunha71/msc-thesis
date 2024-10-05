const isPalindrome = (str) => {
  let len = str.length;
  for (let i = 0; i < len / 2; i++) {
    if (str[i] !== str[len - 1 - i]) {
      return false;
    }
  }
  return true;
}

const makePalindrome = (str) => {
  let len = str.length;
  let middle = len - 1;
  for (let i = 0; i < len; i++) {
    if (isPalindrome(str.slice(i, middle + 1))) {
      return str.slice(0, i) + str.slice(middle, len) + str.slice(i, middle + 1);
    }
  }
  return str;
}
