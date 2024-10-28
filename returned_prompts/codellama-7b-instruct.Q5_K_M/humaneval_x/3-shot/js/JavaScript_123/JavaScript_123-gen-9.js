  var result = [];
  var i = n;

  while (i != 1) {
    if (i % 2 == 1) {
      result.push(i);
    }
    if (i % 2 == 0) {
      i = i / 2;
    } else {
      i = (3 * i) + 1;
    }
  }

  return result;
}



