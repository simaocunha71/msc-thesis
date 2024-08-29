  let result = 0;
  for (const elem of lst) {
    if (elem % 1 === 0 && elem >= 0 && elem % 2 === 1) {
      result += (elem * elem);
    }
  }
  return result;
}



