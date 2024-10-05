  return arr.sort((a, b) => {
    if (a === b) {
      return a - b;
    }
    return (a.toString(2).split('1').length - 1).toString() + a.toString() - (b.toString(2).split('1').length - 1).toString() + b.toString();
  });
}