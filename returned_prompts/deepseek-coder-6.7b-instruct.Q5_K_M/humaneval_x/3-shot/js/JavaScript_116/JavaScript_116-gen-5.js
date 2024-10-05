  return arr.sort((a, b) => {
    let binaryA = a.toString(2);
    let binaryB = b.toString(2);
    let onesA = (binaryA.match(/1/g) || []).length;
    let onesB = (binaryB.match(/1/g) || []).length;
    return onesA - onesB || a - b;
  });
}



