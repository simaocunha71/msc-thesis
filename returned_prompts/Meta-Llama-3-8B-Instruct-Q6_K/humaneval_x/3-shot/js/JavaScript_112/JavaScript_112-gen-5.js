  let result = s.split('');
  for (let i = 0; i < result.length; i++) {
    for (let j = 0; j < c.length; j++) {
      if (result[i] === c[j]) {
        result.splice(i, 1);
        i--;
        break;
      }
    }
  }
  let str = result.join('');
  return [str, isPalindrome(str)];
}

const isPalindrome = (str) => {
  let left = 0;
  let right = str.length - 1;
  while (left < right) {
    if (str[left] !== str[right]) {
      return false;
    }
    left++;
    right--;
  }
  return true;
}
} 