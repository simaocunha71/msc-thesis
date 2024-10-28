  var smallest = lst[0];
  var second_smallest = null;

  for (const elem of lst) {
    if (elem < smallest) {
      second_smallest = smallest;
      smallest = elem;
    }
  }

  return second_smallest;
}



