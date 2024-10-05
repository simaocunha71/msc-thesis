  var result = [number + remaining, 0];

  if (number + remaining >= need) {
    result = [number + remaining - need, need];
  }

  return result;
}



