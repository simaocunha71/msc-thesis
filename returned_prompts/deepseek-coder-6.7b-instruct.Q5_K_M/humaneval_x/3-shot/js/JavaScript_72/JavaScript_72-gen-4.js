  let sum = q.reduce((a, b) => a + b, 0);
  let isBalanced = q.every(val => val === q[0]);
  return sum <= w && isBalanced;
}



