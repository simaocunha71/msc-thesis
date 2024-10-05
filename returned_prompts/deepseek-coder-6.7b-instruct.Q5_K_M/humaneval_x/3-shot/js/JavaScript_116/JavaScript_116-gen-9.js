  return arr.sort((a, b) => {
    let aBin = a.toString(2);
    let bBin = b.toString(2);
    let aOnes = aBin.split('1').length - 1;
    let bOnes = bBin.split('1').length - 1;
    return aOnes - bOnes || a - b;
  });
}



