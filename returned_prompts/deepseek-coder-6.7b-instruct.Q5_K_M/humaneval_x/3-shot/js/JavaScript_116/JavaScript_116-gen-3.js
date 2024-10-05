  return arr.sort((a, b) => {
    let aBinary = a.toString(2);
    let bBinary = b.toString(2);
    let aOnes = aBinary.split('1').length - 1;
    let bOnes = bBinary.split('1').length - 1;
    return aOnes - bOnes || a - b;
  });
}



