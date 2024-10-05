  let result = [];
  let seen = {};

  for (const number of numbers) {
    if (!seen[number]) {
      result.push(number);
      seen[number] = true;
    }
  }

  return result;
}