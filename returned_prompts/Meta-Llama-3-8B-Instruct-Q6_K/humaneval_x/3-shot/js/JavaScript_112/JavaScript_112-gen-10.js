  let result = s.split('');
  for (let i = 0; i < result.length; i++) {
    if (c.includes(result[i])) {
      result.splice(i, 1);
      i--;
    }
  }
  let palindrome = true;
  let left = 0;
  let right = result.length - 1;
  while (left < right) {
    if (result[left] != result[right]) {
      palindrome = false;
      break;
    }
    left++;
    right--;
  }
  return [result.join(''), palindrome];
}