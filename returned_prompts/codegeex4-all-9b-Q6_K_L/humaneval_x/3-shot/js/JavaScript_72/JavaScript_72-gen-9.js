  let sum = 0;
  for (let i = 0; i < q.length; i++) {
    sum += q[i];
  }
  if (sum <= w) {
    let reversed = q.reverse();
    for (let i = 0; i < q.length; i++) {
      if (q[i] != reversed[i]) {
        return false;
      }
    }
    return true;
  }
  return false;
}

