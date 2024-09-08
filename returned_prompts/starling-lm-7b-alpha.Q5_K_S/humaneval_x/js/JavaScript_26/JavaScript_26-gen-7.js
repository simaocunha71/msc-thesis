  let result = [];
  let seen = {};
  for (const n of numbers) {
    if (!(n in seen)) {
      result.push(n);
      seen[n] = true;
    }
  }
  return result;
}



