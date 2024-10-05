  var result = {};
  var words = test.split(' ');

  for (let i = 0; i < words.length; i++) {
    if (result[words[i]] == undefined) {
      result[words[i]] = 1;
    } else {
      result[words[i]] += 1;
    }
  }

  return result;
}

