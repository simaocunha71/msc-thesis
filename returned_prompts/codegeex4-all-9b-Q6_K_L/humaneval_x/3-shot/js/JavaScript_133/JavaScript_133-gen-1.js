  return lst.map(Math.ceil).map(x => x * x).reduce((a, b) => a + b, 0);
}

