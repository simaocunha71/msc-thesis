  var result = [];
  var third_index = 0;

  for (var i = 0; i < l.length; i++) {
    if (i % 3 == 0) {
      result.push(l[i]);
    } else {
      result.push(l[third_index]);
      third_index += 1;
    }
  }

  return result;
}



