  return arr.sort((a, b) => {
    let a1 = a.toString(2);
    let b1 = b.toString(2);
    let a2 = a1.split('1').length - 1;
    let b2 = b1.split('1').length - 1;
    if (a2 != b2) {
      return a2 - b2;
    } else {
      return a - b;
    }
  });
}



