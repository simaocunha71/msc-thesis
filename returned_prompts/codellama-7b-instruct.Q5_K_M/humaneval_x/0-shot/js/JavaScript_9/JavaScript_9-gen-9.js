const rollingMax = (numbers) => {
  const rollingMax = numbers.map((element, index) => {
    const max = Math.max(element, numbers[index - 1]);
    return max;
  });
  return rollingMax;
};

