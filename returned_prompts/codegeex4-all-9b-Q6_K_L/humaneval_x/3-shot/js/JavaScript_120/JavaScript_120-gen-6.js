  let max = Math.max.apply(Math, arr);
  let result = [];
  for (let i = 0; i < k; i++) {
    result.push(max);
  }
  return result;
}



