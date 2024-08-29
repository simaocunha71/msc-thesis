  let sum = q.reduce((a,b) => a + b, 0);
  let max = Math.floor(w / 2);
  return (sum <= max) && (q.join('') === q.reverse().join(''));
}



