  return x
    .filter(n => {
      const digits = String(n).split('').map(Number);
      return digits.every(d => d % 2 !== 0);
    })
    .sort((a, b) => a - b);
}



