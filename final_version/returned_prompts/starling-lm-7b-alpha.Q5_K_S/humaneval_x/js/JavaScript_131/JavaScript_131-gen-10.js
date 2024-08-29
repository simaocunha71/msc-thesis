  let product = 1;
  const digitsArr = String(n).split('').map(Number);

  for (let i = 0; i < digitsArr.length; i++) {
    if (digitsArr[i] % 2 !== 0) {
      product *= digitsArr[i];
    }
  }

  return product;
}



