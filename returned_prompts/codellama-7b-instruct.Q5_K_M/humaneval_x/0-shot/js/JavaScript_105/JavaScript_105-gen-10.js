  const map = [
    'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine'
  ];

  const sorted = arr.sort((a, b) => a - b);
  const filtered = sorted.filter(n => n > 0 && n < 10);
  const reversed = filtered.reverse();
  return reversed.map(n => map[n - 1]);
};
