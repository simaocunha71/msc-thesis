  let result = '';
  for (let i = 0; i < s.length; i++) {
    if (c.indexOf(s[i]) == -1) {
      result += s[i];
    }
  }

  let len = result.length;
  let left = 0;
  let right = len - 1;
  let isPalindrome = true;
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



