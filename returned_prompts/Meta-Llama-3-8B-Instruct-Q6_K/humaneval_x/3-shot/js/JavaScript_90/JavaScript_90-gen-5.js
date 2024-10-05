  if (lst.length < 2) {
    return null;
  }
  let smallest = Infinity;
  let second_smallest = Infinity;
  for (const num of lst) {
    if (num < smallest) {
      second_smallest = smallest;
      smallest = num;
    } else if (num < second_smallest && num !== smallest) {
      second_smallest = num;
    }
  }
  return second_smallest === Infinity ? null : second_smallest;
}