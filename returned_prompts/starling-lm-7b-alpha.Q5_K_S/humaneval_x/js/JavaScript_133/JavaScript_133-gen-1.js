  lst = lst.map(x => Math.ceil(x));
  return lst.reduce((a, b) => a + b * b, 0);
}



