const rollingMax = (numbers) => {
  const result = [];
  numbers.forEach((number, index) => {
    const max = Math.max(number, result[index - 1] || number);
    result.push(max);
  });
  return result;
};
