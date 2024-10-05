  return arr.sort((a, b) => {
    if (a.toString(2).split('1').length > b.toString(2).split('1').length) {
      return 1;
    } else if (a.toString(2).split('1').length < b.toString(2).split('1').length) {
      return -1;
    } else {
      return a - b;
    }
  });
}



