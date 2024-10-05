  return arr.sort((a, b) => {
    const aBinary = a.toString(2);
    const bBinary = b.toString(2);
    const aOnes = aBinary.split('1').length - 1;
    const bOnes = bBinary.split('1').length - 1;

    return aOnes - bOnes || a - b;
  });
}



