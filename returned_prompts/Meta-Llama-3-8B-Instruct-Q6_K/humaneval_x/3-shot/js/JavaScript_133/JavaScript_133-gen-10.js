  return Math.ceil(lst.map(Math.abs).reduce((a, b) => a + b ** 2, 0));
}



