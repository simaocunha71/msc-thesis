  var min = arr.reduce((a, b) => Math.min(a, b));
  if (min % 2 == 1) {
    return [];
  }
  var index = arr.indexOf(min);
  return [min, index];
}