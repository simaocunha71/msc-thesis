  let result = [];
  let stones = n;
  for (let i = 0; i < n; i++) {
    result.push(stones);
    stones = (stones % 2 === 0) ? stones + 2 : stones + 1;
  }
  return result;
}



