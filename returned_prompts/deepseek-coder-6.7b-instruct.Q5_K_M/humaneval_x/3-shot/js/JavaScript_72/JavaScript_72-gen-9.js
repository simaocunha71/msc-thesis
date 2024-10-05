  let sum 		= [...q].reduce((a, b) => a + b, 0);
  let isBalanced = q.every(v => v === q[0]);

  return sum <= w && isBalanced;
}



