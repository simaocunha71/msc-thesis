  if (lst.length < 2) {
    return null;
  }

  var smallest = lst[0];
  var second_smallest = lst[1];

  if (smallest > second_smallest) {
    smallest = lst[1];
    second_smallest = lst[0];
  }

  for (let i = 2; i < lst.length; i++) {
    if (lst[i] < smallest) {
      second_smallest = smallest;
      smallest = lst[i];
    } else if (lst[i] < second_smallest) {
      second_smallest = lst[i];
    }
  }

  if (second_smallest == smallest) {
    return null;
  }

  return second_smallest;
}