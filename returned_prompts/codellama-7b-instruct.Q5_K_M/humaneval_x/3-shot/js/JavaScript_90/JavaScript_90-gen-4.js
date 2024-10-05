  if (lst.length < 2) {
    return null;
  }

  var smallest = lst[0];
  var smallest_index = 0;

  for (var i = 1; i < lst.length; i++) {
    if (lst[i] < smallest) {
      smallest = lst[i];
      smallest_index = i;
    }
  }

  return lst[smallest_index + 1];
}



