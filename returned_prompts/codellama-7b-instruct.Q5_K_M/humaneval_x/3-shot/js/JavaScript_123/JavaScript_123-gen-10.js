  var result = [n];

  while (result[result.length - 1] != 1) {
    if (result[result.length - 1] % 2 == 0) {
      result.push(result[result.length - 1] / 2);
    } else {
      result.push((3 * result[result.length - 1]) + 1);
    }
  }

  return result;
}



