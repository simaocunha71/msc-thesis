  let sum = q.reduce((a, b) => a + b, 0);
  let isBalanced = q.join('') === q.slice().reverse().join('');
  return sum <= w && isBalanced;
}



