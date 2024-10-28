  if (!isPalindrome(q)) return false;
  let sum = q.reduce((a, b) => a + b, 0);
  return sum <= w;
}

const isPalindrome = (q) => {
  return q.join('') === q.join('').split('').reverse().join('');
}