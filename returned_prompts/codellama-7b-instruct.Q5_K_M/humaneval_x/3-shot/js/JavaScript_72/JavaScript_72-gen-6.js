  var total = 0;

  if (q.length == 1) {
    return q[0] <= w;
  }

  for (const i of q) {
    total += i;
  }

  return total <= w && q.join('') == q.join('').split('').reverse().join('');
}



