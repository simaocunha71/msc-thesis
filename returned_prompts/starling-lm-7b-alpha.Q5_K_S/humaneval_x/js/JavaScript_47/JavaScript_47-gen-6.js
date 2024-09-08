  const length = l.length;
  const halfLength = Math.floor(length / 2);
  if (length % 2 === 0) {
    return (l[halfLength] + l[halfLength - 1]) / 2;
  } else {
    return l[halfLength];
  }
}



