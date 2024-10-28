const removeDuplicates = (numbers) => {
  const seen = new Set();
  const result = [];
  numbers.forEach((number) => {
    if (!seen.has(number)) {
      seen.add(number);
      result.push(number);
    }
  });
  return result;
};
