  return arr.sort((a, b) => {
    let binA = a.toString(2);
    let binB = b.toString(2);
    let onesA = (binA.match(/1/g) || []).length;
    let onesB = (binB.match(/1/g) || []).length;

    return onesA - onesB || a - b;
  });
}



