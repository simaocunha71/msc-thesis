  let eaten = need - number;
  let leftover = remaining - eaten;
  if (leftover < 0) {
    eaten += leftover;
    leftover = 0;
  }
  return [eaten + number, leftover];
}



