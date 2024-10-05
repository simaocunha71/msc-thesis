  if (lst.length < 2) {
    return null;
  }

  let min = lst[0];
  let second_min = lst[0];

  for (const num of lst) {
    if (num < min) {
      second_min = min;
      min = num;
    } else if (num < second_min && num != min) {
      second_min = num;
    }
  }

  if (second_min == min) {
    return null;
  } else {
    return second_min;
  }
}