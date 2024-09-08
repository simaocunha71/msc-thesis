  let min = lst[0];
  let min2 = lst[0];

  for (const elem of lst) {
    if (elem < min) {
      min2 = min;
      min = elem;
    } else if (elem < min2 && elem != min) {
      min2 = elem;
    }
  }

  if (min2 == lst[0]) return null;
  return min2;
}



