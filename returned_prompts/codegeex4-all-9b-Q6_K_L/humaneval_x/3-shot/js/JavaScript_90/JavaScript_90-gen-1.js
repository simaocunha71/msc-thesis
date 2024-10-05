  let smallest = Number.MAX_SAFE_INTEGER;
  let second_smallest = Number.MAX_SAFE_INTEGER;

  for (const n of lst) {
    if (n < smallest) {
      second_smallest = smallest;
      smallest = n;
    } else if (n < second_smallest) {
      second_smallest = n;
    }
  }

  return second_smallest == Number.MAX_SAFE_INTEGER ? null : second_smallest;
}