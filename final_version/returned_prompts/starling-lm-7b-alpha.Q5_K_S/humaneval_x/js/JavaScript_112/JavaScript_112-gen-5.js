  let result = s;
  for (const char of c) {
    result = result.replace(char, '');
  }

  let isPalindrome = true;
  for (let i = 0; i < result.length / 2; i++) {
    if (result[i] !== result[result.length - 1 - i]) {
      isPalindrome = false;
      break;
    }
  }

  return [result, isPalindrome];
}



