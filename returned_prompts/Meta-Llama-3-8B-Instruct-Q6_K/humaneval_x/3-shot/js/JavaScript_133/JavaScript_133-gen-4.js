  return Math.round(Math.ceil(lst.map(Math.abs).map(Math.pow.bind(null, 2))).reduce((a, b) => a + b, 0));
}