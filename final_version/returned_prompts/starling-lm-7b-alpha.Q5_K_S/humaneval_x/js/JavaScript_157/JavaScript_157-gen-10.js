  let sides = [a, b, c];
  sides.sort(function(a, b) { return a - b; });
  return (sides[0] * sides[0] + sides[1] * sides[1]) == sides[2] * sides[2];
}



