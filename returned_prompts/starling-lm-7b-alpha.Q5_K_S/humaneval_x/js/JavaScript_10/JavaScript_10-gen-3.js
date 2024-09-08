  const isPal = (str) => str == str.split('').reverse().join('');
  const longestPalindrome = (str) => {
    let result = '';
    for (let i = 1; i < str.length; i++) {
      let subStr = str.slice(i, i + result.length + 1);
      if (isPal(subStr)) {
        result = subStr;
      }
    }
    return result;
  };

  return string + longestPalindrome(string.slice(0, string.length - longestPalindrome(string).length));
}



