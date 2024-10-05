  const names = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine'];
  const sorted = arr.sort((a, b) => a - b);
  const result = [];

  for (let i = 0; i < sorted.length; i++) {
    if (sorted[i] >= 1 && sorted[i] <= 9) {
      result.push(names[sorted[i] - 1]);
    }
  }

  return result;
}



