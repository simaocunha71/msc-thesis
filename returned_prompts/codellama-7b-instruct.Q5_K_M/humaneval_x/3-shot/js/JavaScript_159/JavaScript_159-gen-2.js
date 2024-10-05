  var eaten = number;
  var left = remaining - number;

  if (left < need) {
    eaten += left;
    left = 0;
  } else {
    eaten += need;
    left -= need;
  }

  return [eaten, left];
}



