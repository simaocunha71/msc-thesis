  let sides = [a, b, c].sort((a, b) => a - b);
  return Math.abs(sides[0]*sides[0] + sides[1]*sides[1] - sides[2]*sides[2]) < 0.00001;
}



