  const clone = [...array];

  let sum = clone[0] + clone[clone.length - 1];
  clone.sort((a, b) => {
    if (sum % 2 === 0) {
      return b - a;
    } else {
      return a - b;
    }
  });

  return clone;
}



