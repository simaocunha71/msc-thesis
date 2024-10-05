  if (lst.length < 2) {
    return null;
  }

  var smallest = lst[0];
  var second_smallest = lst[1];

  for (const i of lst) {
    if (i < smallest) {
      second_smallest = smallest;
      smallest = i;
    } else if (i < second_smallest && i != smallest) {
      second_smallest = i;
    }
  }

  if (second_smallest == smallest) {
    return null;
  } else {
    return second_smallest;
  }
}