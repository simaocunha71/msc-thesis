const isPalindrome = (text) => {
  return text.toLowerCase() === text.toLowerCase().split('').reverse().join('');
};
