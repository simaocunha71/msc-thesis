  let sum = q.reduce((a, b) => a + b, 0);
  let isBalanced = q.toString() === q.reverse().toString();

  if (sum <= w && isBalanced) {
    return true;
  } else {
    return false;
  }
}



