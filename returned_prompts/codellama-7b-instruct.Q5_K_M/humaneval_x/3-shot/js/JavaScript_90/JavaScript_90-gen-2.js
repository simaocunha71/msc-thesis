  if (lst.length < 2) {
    return null;
  }

  let smallest = lst[0];
  let next_smallest = null;

  for (let i = 1; i < lst.length; i++) {
    if (lst[i] < smallest) {
      next_smallest = smallest;
      smallest = lst[i];
    }
  }

  return next_smallest;
}



