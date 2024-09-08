  const result = [];
  for (let i = a; i <= b; i++) {
    const str_i = i.toString();
    for (const digit of str_i) {
      if (Number(digit) % 2 == 0) {
        result.push(Number(digit));
      }
    }
  }
  return result.sort((a, b) => a - b);
}



