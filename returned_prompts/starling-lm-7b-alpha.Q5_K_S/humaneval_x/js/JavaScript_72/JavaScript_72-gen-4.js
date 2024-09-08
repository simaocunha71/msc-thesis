  let sum = q.reduce((acc, cur) => acc + cur, 0);
  let length = q.length;
  return (sum <= w) && (length % 2 === 1);
}



