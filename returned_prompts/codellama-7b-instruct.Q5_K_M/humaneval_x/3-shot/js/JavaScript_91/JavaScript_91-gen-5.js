  var result = 0;

  for (let sentence of S.split(/\.|\?|\!/)) {
    if (sentence.startsWith('I')) {
      result += 1;
    }
  }

  return result;
}



