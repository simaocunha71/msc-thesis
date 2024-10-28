  return Math.round(Math.ceil(lst.map(Math.abs).map(Math.pow)).reduce((a, b) => a + b, 0));
}