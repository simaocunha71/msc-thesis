  var sides = [a, b, c].sort((a, b) => a - b);
  return Math.pow(sides[2], 2) == Math.pow(sides[0], 2) + Math.pow(sides[1], 2);
}



