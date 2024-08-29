  let sum = q.reduce((total, current) => total + current, 0);
  let reversed = q.slice(0).reverse();
  return sum <= w && q.join('') === reversed.join('');
}



