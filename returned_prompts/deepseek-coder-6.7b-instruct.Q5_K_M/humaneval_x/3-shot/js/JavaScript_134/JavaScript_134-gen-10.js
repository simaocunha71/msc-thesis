  const lastChar = txt.slice(-1);
  const penultimateChar = txt.slice(-2, -1);

  return /[a-z]/i.test(lastChar) && !/[a-z]/i.test(penultimateChar);
}



