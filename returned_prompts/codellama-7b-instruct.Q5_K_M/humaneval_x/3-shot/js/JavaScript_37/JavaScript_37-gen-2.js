  var result = [];
  var even_indexes = [];
  var odd_indexes = [];
  for (var i = 0; i < l.length; i++) {
    if (i % 2 == 0) {
      even_indexes.push(i);
    } else {
      odd_indexes.push(i);
    }
  }

  for (var i = 0; i < even_indexes.length; i++) {
    result[even_indexes[i]] = l[even_indexes[i]];
  }

  for (var i = 0; i < odd_indexes.length; i++) {
    result[odd_indexes[i]] = l[odd_indexes[i]];
  }

  return result;
}



