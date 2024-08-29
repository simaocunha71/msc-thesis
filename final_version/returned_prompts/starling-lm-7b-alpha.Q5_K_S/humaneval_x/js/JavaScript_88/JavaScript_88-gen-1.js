  const sum = array[0] + array[array.length - 1];
  const isOdd = sum % 2;

  const clone = [...array];
  clone.sort((a, b) => {
    return (isOdd ? 1 : -1) * (a - b);
  });

  return clone;
};



