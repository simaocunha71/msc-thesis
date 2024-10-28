function willItFly(q, w) {
  if (q.join('') === q.reverse().join('') && q.reduce((a, b) => a + b) <= w) {
    return true;
  }
  return false;
}

