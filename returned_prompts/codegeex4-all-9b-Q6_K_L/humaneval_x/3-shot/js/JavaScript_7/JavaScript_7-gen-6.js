  var result = [];
  for (const str of strings) {
    if (str.indexOf(substring) != -1) {
      result.push(str);
    }
  }
  return result;
}



