  if (q.length % 2 == 1) {
    return false;
  }

  let sum = 0;
  let reversed_q = q.slice().reverse();

  for (let i = 0; i < q.length; i++) {
    sum += q[i] + reversed_q[i];
    if (sum > w) {
      return false;
    }
  }

  return true;
}

