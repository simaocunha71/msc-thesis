  let result = [];

  for(let i = 0; i < n; i++) {
    if(n % 2 === 0) {
      result.push(2 * (i + 1));
    } else {
      result.push(2 * (i + 1) - 1);
    }
  }

  return result;
}



