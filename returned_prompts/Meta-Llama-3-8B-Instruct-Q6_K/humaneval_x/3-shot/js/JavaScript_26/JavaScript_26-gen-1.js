  let seen = {};
  let result = [];

  for (let i = 0; i < numbers.length; i++) {
    let n = numbers[i];
    if (!seen[n]) {
      result.push(n);
      seen[n] = true;
    }
  }

  return result;
}

