  var result = 0;
  var words = S.split(/[\.\?!]/);
  for (const word of words) {
    if (word.trim().startsWith('I')) {
      result += 1;
    }
  }
  return result;
}