  let sum = q.reduce((sum, el) => sum + el, 0);
  return q.slice(0, Math.floor(q.length / 2)).reverse().join('') === q.slice(q.length / 2).join('') && sum <= w;
}



