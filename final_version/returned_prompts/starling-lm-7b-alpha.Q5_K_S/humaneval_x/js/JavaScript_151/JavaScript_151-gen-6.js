  let total = 0;
  for (const elem of lst) {
    if (typeof elem === 'number' && elem >= 0 && elem % 1 === 0 && elem % 2 === 1) {
      total += elem * elem;
    }
  }
  return total;
}



