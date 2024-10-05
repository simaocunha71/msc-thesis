  var dict = {};
  var words = test.split(' ');

  for (var word of words) {
    if (word in dict) {
      dict[word] += 1;
    } else {
      dict[word] = 1;
    }
  }

  var max = 0;
  var maxes = [];
  for (var key in dict) {
    if (dict[key] > max) {
      max = dict[key];
    }
  }

  for (var key in dict) {
    if (dict[key] == max) {
      maxes.push(key);
    }
  }

  return dict;
}



