  return Math.round(lst.map(Math.ceil).map(Math.pow).reduce((a, b) => a + b, 0));
}