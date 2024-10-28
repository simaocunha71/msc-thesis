  return arr.sort((a, b) => {
    const binA = a.toString(2);
    const binB = b.toString(2);
    const onesA = binA.split('1').length - 1;
    const onesB = binB.split('1').length - 1;
    if (onesA == onesB) {
      return a - b;
    }
    return onesA - onesB;
  });
}



