  var minEven = Math.min(...arr.filter(x => x % 2 == 0));
  if (minEven == Infinity) return [];
  return [minEven, arr.indexOf(minEven)];
}