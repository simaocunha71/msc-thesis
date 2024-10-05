  let sum = q.reduce((a, b) => a + b, 0);
  let isBalanced = q.toString() === q.toString().split('').reverse().join('');
  return sum <= w && isBalanced;
}