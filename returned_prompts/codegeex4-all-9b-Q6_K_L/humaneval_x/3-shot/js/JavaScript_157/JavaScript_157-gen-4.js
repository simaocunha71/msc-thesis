  let sides = [a, b, c].sort();
  let hypotenuse = sides[2];
  let opposite = sides[1];
  let adjacent = sides[0];

  return Math.pow(hypotenuse, 2) == Math.pow(opposite, 2) + Math.pow(adjacent, 2);
}