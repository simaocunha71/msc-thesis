  if (q.length % 2 !== 0) {
    return false;
  }

  let sum = 0;
  for (let i = 0; i < q.length / 2; i++) {
    sum += q[i] + q[q.length - 1 - i];
  }

  return sum <= w;
}



