  var largest_negative_integer = null;
  var smallest_positive_integer = null;

  for (var i = 0; i < lst.length; i++) {
    if (lst[i] < 0 && largest_negative_integer == null) {
      largest_negative_integer = lst[i];
    } else if (lst[i] < 0 && lst[i] > largest_negative_integer) {
      largest_negative_integer = lst[i];
    }

    if (lst[i] > 0 && smallest_positive_integer == null) {
      smallest_positive_integer = lst[i];
    } else if (lst[i] > 0 && lst[i] < smallest_positive_integer) {
      smallest_positive_integer = lst[i];
    }
  }

  return [largest_negative_integer, smallest_positive_integer];
}



