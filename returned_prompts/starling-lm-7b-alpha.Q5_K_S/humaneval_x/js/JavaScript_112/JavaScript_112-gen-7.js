  let result = s;
  for (const char of c) {
    while (result.includes(char)) {
      result = result.replace(char, '');
    }
  }

  const isPalindrome = () => {
    let left = 0;
    let right = result.length - 1;
    while (left < right) {
      if (result[left] !== result[right]) {
        return false;
      }
      left += 1;
      right -= 1;
    }
    return true;
  }

  return [result, isPalindrome()];
}



