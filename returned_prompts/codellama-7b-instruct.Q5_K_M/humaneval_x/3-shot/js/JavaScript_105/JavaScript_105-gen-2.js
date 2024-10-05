  const names = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine'];
  const result = [];

  for (const digit of arr) {
    if (digit >= 1 && digit <= 9) {
      result.push(names[digit - 1]);
    }
  }

  return result;
}



