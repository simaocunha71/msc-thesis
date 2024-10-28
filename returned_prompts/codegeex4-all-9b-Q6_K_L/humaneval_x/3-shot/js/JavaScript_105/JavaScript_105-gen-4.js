  const digits = arr.filter((n) => n >= 1 && n <= 9);
  return digits.sort().reverse().map((n) => String(n));
};

const toNames = (arr) => {
  const map = new Map([
    [1, 'One'],
    [2, 'Two'],
    [3, 'Three'],
    [4, 'Four'],
    [5, 'Five'],
    [6, 'Six'],
    [7, 'Seven'],
    [8, 'Eight'],
    [9, 'Nine'],
  ]);
  return arr.map((n) => map.get(n));
};

const solve = (arr) => {
  if (arr.length === 0) {
    return [];
  }
  return toNames(byLength(arr));
};

