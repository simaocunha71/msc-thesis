  const result = [];

  for (let i = a; i <= b; i++) {
    const digits = i.toString();
    for (const digit of digits) {
      if (parseInt(digit) % 2 === 0) {
        result.push(parseInt(digit));
      }
    }
  }

  return result;
}



