  var isSorted = true;
  for (var i = 0; i < lst.length - 1; i++) {
    if (lst[i] > lst[i + 1]) {
      isSorted = false;
      break;
    }
  }
  return isSorted;
}