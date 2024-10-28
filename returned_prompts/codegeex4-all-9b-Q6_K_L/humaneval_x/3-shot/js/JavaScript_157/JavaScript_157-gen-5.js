  let sides = [a, b, c];
  sides = sides.sort((a, b) => a - b);
  return sides[0] ** 2 + sides[1] ** 2 === sides[2] ** 2;
}

