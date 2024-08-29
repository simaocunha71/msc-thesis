  if (lst.length < 2) {
    return null;
  }

  let smallest = lst[0];
  let second_smallest = lst[0];
  for (const i of lst) {
    if (i < smallest) {
      second_smallest = smallest;
      smallest = i;
    } else if (i < second_smallest && i != smallest) {
      second_smallest = i;
    }
  }

  return second_smallest;
}



