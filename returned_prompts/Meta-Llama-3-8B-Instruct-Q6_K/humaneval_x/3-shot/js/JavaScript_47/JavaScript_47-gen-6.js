  l.sort((a, b) => a - b);
  let length = l.length;
  if (length % 2 === 0) {
    return (l[length / 2 - 1] + l[length / 2]) / 2;
  } else {
    return l[Math.floor(length / 2)];
  }
}