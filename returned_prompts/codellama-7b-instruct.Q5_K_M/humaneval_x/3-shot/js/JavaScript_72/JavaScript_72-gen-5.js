  if (q.join('').split('').reverse().join('') == q.join('')) {
    if (q.reduce((a, b) => a + b) <= w) {
      return true;
    }
  }
  return false;
}



