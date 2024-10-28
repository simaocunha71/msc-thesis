  arr.sort((a, b) => {
    const aBin = a.toString(2);
    const bBin = b.toString(2);
    const aOnes = aBin.split('1').length - 1;
    const bOnes = bBin.split('1').length - 1;
    if (aOnes === bOnes) {
      return a - b;
    }
    return aOnes - bOnes;
  });
  return arr;
}



