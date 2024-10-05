  return arr.sort((a, b) => {
    const binaryA = a.toString(2);
    const binaryB = b.toString(2);
    const onesA = (binaryA.match(/1/g) || []).length;
    const onesB = (binaryB.match(/1/g) || []).length;
    return onesA - onesB || a - b;
  });
}



