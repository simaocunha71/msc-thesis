  return arr.sort((a, b) => {
    let aBinary = a.toString(2);
    let bBinary = b.toString(2);
    let aOnes = (aBinary.match(/1/g) || []).length;
    let bOnes = (bBinary.match(/1/g) || []).length;
    return aOnes - bOnes || a - b;
  });
}



