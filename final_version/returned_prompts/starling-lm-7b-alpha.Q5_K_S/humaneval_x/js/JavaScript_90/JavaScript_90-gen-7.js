  if (lst.length < 2) {
    return null;
  }

  let smallest = Infinity;
  let second_smallest = Infinity;

  for (const x of lst) {
    if (x < smallest) {
      second_smallest = smallest;
      smallest = x;
    } else if (x < second_smallest && x != smallest) {
      second_smallest = x;
    }
  }

  return second_smallest;
}



