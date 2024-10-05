  let sequence = [];
  let curr = n;

  while (curr != 1) {
    if (curr % 2 == 1) {
      sequence.push(curr);
    }
    if (curr % 2 == 0) {
      curr = curr / 2;
    } else {
      curr = curr * 3 + 1;
    }
  }

  sequence.push(1);
  return sequence.sort((a, b) => a - b);
}