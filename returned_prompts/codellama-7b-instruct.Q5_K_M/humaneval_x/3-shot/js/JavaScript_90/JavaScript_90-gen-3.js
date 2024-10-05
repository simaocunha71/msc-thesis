  if (lst.length < 2) {
    return null;
  }

  var second_smallest = null;
  var smallest = lst[0];

  for (const element of lst) {
    if (element < smallest) {
      second_smallest = smallest;
      smallest = element;
    } else if (element > smallest && (second_smallest == null || element < second_smallest)) {
      second_smallest = element;
    }
  }

  return second_smallest;
}



