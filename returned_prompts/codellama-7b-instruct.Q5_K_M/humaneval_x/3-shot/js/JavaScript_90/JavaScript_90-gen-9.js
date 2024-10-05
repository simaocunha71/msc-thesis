  if (lst.length < 2) {
    return null;
  }
  var smallest = lst[0];
  var i = 1;
  while (i < lst.length) {
    if (lst[i] < smallest) {
      smallest = lst[i];
    }
    i += 1;
  }
  var second_smallest = null;
  i = 0;
  while (i < lst.length) {
    if (lst[i] == smallest) {
      second_smallest = lst[i+1];
      break;
    }
    i += 1;
  }
  return second_smallest;
}



