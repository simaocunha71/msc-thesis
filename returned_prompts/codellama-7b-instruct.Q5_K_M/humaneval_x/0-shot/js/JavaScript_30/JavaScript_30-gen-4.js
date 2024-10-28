const getPositive = (list) => {
  const positive = [];
  list.forEach(number => {
    if (number > 0) {
      positive.push(number);
    }
  });
  return positive;
}

