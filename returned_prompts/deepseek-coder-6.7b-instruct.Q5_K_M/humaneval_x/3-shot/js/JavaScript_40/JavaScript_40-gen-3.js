  if (l.length < 3) return false;

  l.sort((a, b) => a - b);

  for (let i = 0; i < l.length - 2; i++) {
    let start = i + 1;
    let end = l.length - 1;

    while (start < end) {
      let sum = l[i] + l[start] + l[end];

      if (sum === 0) return true;
      else if (sum < 0) start += 1;
      else end -= 1;
    }
  }

  return false;
}



