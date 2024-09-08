  let sum = q.reduce((sum, el) => sum + el, 0);
  return sum <= w && q.slice(0, Math.floor(q.length / 2)).join('') === q.slice(q.length - Math.floor(q.length / 2)).reverse().join('');
}



