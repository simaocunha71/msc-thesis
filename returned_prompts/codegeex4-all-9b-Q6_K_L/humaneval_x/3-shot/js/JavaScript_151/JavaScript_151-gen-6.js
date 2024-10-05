  let result = 0;

  for (const e of lst) {
    if (e % 2 == 1 && e >= 0 && Number.isInteger(e)) {
      result += e * e;
    }
  }

  return result;
}

