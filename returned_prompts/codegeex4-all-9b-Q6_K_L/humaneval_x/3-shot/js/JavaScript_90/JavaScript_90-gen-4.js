  if (lst.length < 2) {
    return null;
  }
  let smallest = lst[0];
  let second_smallest = lst[1];
  if (second_smallest < smallest) {
    [smallest, second_smallest] = [second_smallest, smallest];
  }
  for (const n of lst) {
    if (n < smallest) {
      [smallest, second_smallest] = [n, smallest];
    } else if (n > smallest && n < second_smallest) {
      second_smallest = n;
    }
  }
  if (second_smallest == smallest) {
    return null;
  } else {
    return second_smallest;
  }
}