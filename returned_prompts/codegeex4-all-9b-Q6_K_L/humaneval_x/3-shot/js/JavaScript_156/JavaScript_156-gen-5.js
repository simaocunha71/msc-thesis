  const map = [
    [10, 'x'],
    [9, 'ix'],
    [5, 'v'],
    [4, 'iv'],
    [1, 'i'],
  ];

  let result = '';
  for (const [value, symbol] of map) {
    while (number >= value) {
      result += symbol;
      number -= value;
    }
  }

  return result;
}