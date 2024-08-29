  const result = [];
  for (let i = Math.min(a, b); i <= Math.max(a, b); i++) {
    const number = i.toString();
    for (const digit of number) {
      if (parseInt(digit) % 2 === 0) {
        result.push(parseInt(digit));
      }
    }
  }
  return result;
}



