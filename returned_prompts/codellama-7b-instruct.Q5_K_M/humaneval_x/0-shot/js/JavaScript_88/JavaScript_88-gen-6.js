

  const arr = [...array];
  const sum = arr[0] + arr[arr.length - 1];
  if (sum % 2 === 0) {
    return arr.sort((a, b) => b - a);
  }
  return arr.sort((a, b) => a - b);

};
