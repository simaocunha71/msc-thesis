  var result = [];
  for (let length = 1; length <= string.length; length++) {
    result.push(string.substring(0, length));
  }
  return result;
}