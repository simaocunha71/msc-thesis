  const numNames = {
    1: 'One',
    2: 'Two',
    3: 'Three',
    4: 'Four',
    5: 'Five',
    6: 'Six',
    7: 'Seven',
    8: 'Eight',
    9: 'Nine'
  };

  const filtered = arr.filter(n => n >= 1 && n <= 9).sort((a, b) => a - b).reverse();
  return filtered.map(n => numNames[n]);
}