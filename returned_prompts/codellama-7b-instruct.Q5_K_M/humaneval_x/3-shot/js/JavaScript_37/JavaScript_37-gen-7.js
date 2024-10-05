  var result = [];
  var even_list = [];
  for (var i = 0; i < l.length; i++) {
    if (i % 2 == 0) {
      even_list.push(l[i]);
    } else {
      result.push(even_list.sort()[0]);
      even_list = [];
    }
  }

  return result;
}



