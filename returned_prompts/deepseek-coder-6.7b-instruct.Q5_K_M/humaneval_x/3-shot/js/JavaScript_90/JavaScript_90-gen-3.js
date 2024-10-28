  let smallest = null;
  let secondSmallest = null;
  for (let i = 0; i < lst.length; i++) {
    let current = lst[i];
    if (smallest === null || current < smallest) {
      secondSmallest = smallest;
      smallest = current;
    } else if (current > smallest && (secondSmallest === null || current < secondSmallest)) {
      secondSmallest = current;
    }
  }
  return secondSmallest;
}



