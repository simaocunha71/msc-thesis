const isPalindrome = (text) => {
  return text.toLowerCase().split('').reverse().join('') === text.toLowerCase();
};
