  let smallest = Number.MAX_SAFE_INTEGER;
  let second_smallest = Number.MAX_SAFE_INTEGER;

  for (let i = 0; i < lst.length; i++) {
    if (lst[i] < smallest) {
      second_smallest = smallest;
      smallest = lst[i];
    } else if (lst[i] < second_smallest && lst[i] > smallest) {
      second_smallest = lst[i];
    }
  }

  return (second_smallest == Number.MAX_SAFE_INTEGER) ? null : second_smallest;
}



