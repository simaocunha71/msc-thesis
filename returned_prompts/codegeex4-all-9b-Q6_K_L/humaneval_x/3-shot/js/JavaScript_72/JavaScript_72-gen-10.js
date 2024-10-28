  let sum = q.reduce((a, b) => a + b, 0);
  let reversed_q = q.slice().reverse();
  if (sum <= w && JSON.stringify(q) === JSON.stringify(reversed_q)) {
    return true;
  } else {
    return false;
  }
}