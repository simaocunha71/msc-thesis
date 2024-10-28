  let sides = [a, b, c];
  sides.sort((x, y) => x - y);

  let a2 = sides[0] * sides[0];
  let b2 = sides[1] * sides[1];
  let c2 = sides[2] * sides[2];

  return a2 + b2 == c2;
}



