  return arr.sort((a, b) => {
    let countOnesA = (a >>> 0).toString(2).split('1').length - 1;
    let countOnesB = (b >>> 0).toString(2).split('1').length - 1;
    return countOnesA - countOnesB || a - b;
  });
}



