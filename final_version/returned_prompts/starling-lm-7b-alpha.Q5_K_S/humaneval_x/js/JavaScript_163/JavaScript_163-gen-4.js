  const digits = String(a).split('').map(x => Number(x));
  const digits_b = String(b).split('').map(x => Number(x));

  const result = [];

  for (let i = Math.min(...digits); i <= Math.min(...digits_b); i++) {
    if (i % 2 === 0) {
      result.push(i);
    }
  }

  return result;
}



