const removeDuplicates = (numbers) => {
  let seen = new Set();
  let result = [];

  for (let num of numbers) {
    if (!seen.has(num)) {
      seen.add(num);
      result.push(num);
    }
  }
  return result;
}

