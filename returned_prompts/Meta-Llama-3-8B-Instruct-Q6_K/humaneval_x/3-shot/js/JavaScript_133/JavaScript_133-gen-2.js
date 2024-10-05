  return Math.round(lst.map(Math.ceil).map(x => x ** 2).reduce((a, b) => a + b, 0));
}