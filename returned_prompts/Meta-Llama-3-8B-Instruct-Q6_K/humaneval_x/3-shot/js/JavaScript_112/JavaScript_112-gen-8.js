  let result = '';
  for (let i = 0; i < s.length; i++) {
    if (!c.includes(s[i])) {
      result += s[i];
    }
  }
  let isPalindrome = true;
  let left = 0;
  let right = result.length - 1;
  while (left < right) {
    if (result[left] !== result[right]) {
      isPalindrome = false;
      break;
    }
    left++;
    right--;
  }
  return [result, isPalindrome];
}