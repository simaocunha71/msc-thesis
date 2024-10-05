  var largest = null;
  var smallest = null;

  for (var i = 0; i < lst.length; i++) {
    if (lst[i] < 0) {
      if (largest == null) {
        largest = lst[i];
      } else if (lst[i] > largest) {
        largest = lst[i];
      }
    }
    if (lst[i] > 0) {
      if (smallest == null) {
        smallest = lst[i];
      } else if (lst[i] < smallest) {
        smallest = lst[i];
      }
    }
  }

  return [largest, smallest];
}



