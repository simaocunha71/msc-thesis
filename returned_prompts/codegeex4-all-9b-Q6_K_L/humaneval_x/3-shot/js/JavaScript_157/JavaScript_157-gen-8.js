  var sides = [a, b, c];
  sides.sort((a, b) => a - b);

  if (sides[0] * sides[0] + sides[1] * sides[1] == sides[2] * sides[2]) {
    return true;
  } else {
    return false;
  }
}



