  const isBalanced = (q) => {
    const mid = Math.floor(q.length / 2);
    for (let i = 0; i < mid; i++) {
      if (q[i] !== q[q.length - 1 - i]) {
        return false;
      }
    }
    return true;
  }

  const sum = q.reduce((a, b) => a + b, 0);
  return isBalanced(q) && sum <= w;
}



