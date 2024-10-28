  return values.filter(x => typeof x === 'number' && parseInt(x) === x);
}  // parseInt(x) === x is a trick to filter out floats, as parseInt(float) returns NaN, and NaN is not equal to any number



