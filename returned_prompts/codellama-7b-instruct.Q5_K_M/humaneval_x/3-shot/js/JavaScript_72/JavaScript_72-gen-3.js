  if (q.length == 1) {
    return w >= q[0];
  } else if (q.length == 2) {
    return w >= q[0] + q[1];
  } else {
    if (q[0] == q[q.length - 1]) {
      return willItFly(q.slice(1, q.length - 1), w);
    }
  }
}



