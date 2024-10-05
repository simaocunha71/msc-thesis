  var result = {};
  var words = test.split(" ");

  for (var i = 0; i < words.length; i++) {
    if (words[i] in result) {
      result[words[i]] += 1;
    } else {
      result[words[i]] = 1;
    }
  }

  return result;
}

