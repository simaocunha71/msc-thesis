  return lst.map(number => Math.ceil(number)).map(number => number * number).reduce((a, b) => a + b);
}



