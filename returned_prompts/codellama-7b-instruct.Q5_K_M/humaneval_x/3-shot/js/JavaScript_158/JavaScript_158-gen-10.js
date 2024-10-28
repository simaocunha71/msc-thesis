  var max = 0;
  var result = "";
  for (const word of words) {
    if (word.length > max) {
      max = word.length;
      result = word;
    }
  }
  return result;
}



