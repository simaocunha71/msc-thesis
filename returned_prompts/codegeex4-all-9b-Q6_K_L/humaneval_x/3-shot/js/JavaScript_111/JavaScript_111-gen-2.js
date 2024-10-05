  var result = {};
  var count = 0;
  var max = 0;
  var words = test.split(' ');

  for (var i = 0; i < words.length; i++) {
    if (words[i] in result) {
      result[words[i]] += 1;
    } else {
      result[words[i]] = 1;
    }
  }

  for (var key in result) {
    if (result[key] > max) {
      max = result[key];
    }
  }

  for (var key in result) {
    if (result[key] != max) {
      delete result[key];
    }
  }

  return result;
}



