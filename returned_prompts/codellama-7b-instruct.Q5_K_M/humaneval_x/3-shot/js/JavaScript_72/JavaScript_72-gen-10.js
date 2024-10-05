  if (q.join('') == q.join('').split('').reverse().join('')) {
    let sum = 0;
    for (let i = 0; i < q.length; i++) {
      sum += q[i];
    }
    if (sum <= w) {
      return true;
    }
  }
  return false;
}



