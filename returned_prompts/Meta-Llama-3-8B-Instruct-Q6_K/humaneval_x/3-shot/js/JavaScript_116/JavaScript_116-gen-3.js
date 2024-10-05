  return arr.sort((a, b) => {
    if (a.toString().split('1').length - 1 !== b.toString().split('1').length - 1) {
      return a.toString().split('1').length - 1 - b.toString().split('1').length - 1;
    } else {
      return a - b;
    }
  });
}