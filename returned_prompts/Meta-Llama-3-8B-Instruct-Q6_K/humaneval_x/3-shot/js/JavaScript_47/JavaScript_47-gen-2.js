  l.sort((a, b) => a - b);
  let middleIndex = Math.floor(l.length / 2);
  if (l.length % 2 === 0) {
    return (l[middleIndex - 1] + l[middleIndex]) / 2;
  } else {
    return l[middleIndex];
  }
}