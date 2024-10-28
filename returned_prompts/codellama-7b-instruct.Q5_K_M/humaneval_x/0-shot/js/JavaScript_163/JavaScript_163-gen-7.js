  const numbers = [];

  for (let i = a; i <= b; i++) {
    if (i % 2 === 0) {
      numbers.push(i);
    }
  }

  return numbers.sort((a, b) => a - b);
};
