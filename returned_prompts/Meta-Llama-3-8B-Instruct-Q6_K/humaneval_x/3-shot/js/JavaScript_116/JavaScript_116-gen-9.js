  return arr.sort((a, b) => {
    if (a.toString(2).split('1').length - 1 === b.toString(2).split('1').length - 1) {
      return a - b;
    } else {
      return a.toString(2).split('1').length - 1 - b.toString(2).split('1').length + 1;
    }
  });
}