  if (lst.length < 2) {
    return null;
  }

  let smallest = lst[0];
  let second_smallest = lst[1];

  if (smallest > second_smallest) {
    let temp = smallest;
    smallest = second_smallest;
    second_smallest = temp;
  }

  for (let i = 2; i < lst.length; i++) {
    if (lst[i] < smallest) {
      second_smallest = smallest;
      smallest = lst[i];
    } else if (lst[i] < second_smallest) {
      second_smallest = lst[i];
    }
  }

  return second_smallest;
}



