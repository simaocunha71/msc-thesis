  let sides = [a, b, c];
  sides.sort(function(a, b) {
    return a - b;
  });
  let largest = sides[2];
  let sum = sides[0] + sides[1];
  return sum > largest;
}