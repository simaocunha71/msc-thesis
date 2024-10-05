  if (q.length == 1) {
    return q[0] <= w;
  }
  if (q.length == 2) {
    return q[0] + q[1] <= w;
  }
  if (q.length == 3) {
    return q[0] + q[1] + q[2] <= w;
  }

  if (q.length % 2 == 0) {
    return q.reduce((prev, cur) => prev + cur, 0) <= w;
  } else {
    return q.reduce((prev, cur) => prev + cur, 0) <= w &&
      (q.slice(0, q.length / 2).reduce((prev, cur) => prev + cur, 0) ==
      q.slice(q.length / 2).reduce((prev, cur) => prev + cur, 0));
  }
}



