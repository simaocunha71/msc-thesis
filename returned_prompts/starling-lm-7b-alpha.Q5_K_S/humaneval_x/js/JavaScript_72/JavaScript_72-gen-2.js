  let sum = q.reduce((acc, curr) => acc + curr, 0);
  let mid = Math.floor(q.length / 2);
  let left = q.slice(0, mid);
  let right = q.slice(mid);

  return (sum <= w) && JSON.stringify(left) === JSON.stringify(right);
}



