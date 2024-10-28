  var result = 0;
  var length = lst.length;
  for (var i = 0; i < length; i += 2) {
    if (lst[i] % 2 != 0) {
      result += lst[i];
    }
  }
  return result;
}



