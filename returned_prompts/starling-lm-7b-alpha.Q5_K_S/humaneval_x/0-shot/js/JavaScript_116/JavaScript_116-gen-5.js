  return arr.sort((a, b) => (
    a.toString(2).length - b.toString(2).length ||
    a.toString(2).split('1').length - b.toString(2).split('1').length ||
