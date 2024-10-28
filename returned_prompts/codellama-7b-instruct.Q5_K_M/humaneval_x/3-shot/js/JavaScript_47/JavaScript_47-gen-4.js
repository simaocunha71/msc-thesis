  l.sort();

  const middle = Math.floor(l.length / 2);

  if (l.length % 2 === 0) {
    return (l[middle - 1] + l[middle]) / 2.0;
  } else {
    return l[middle];
  }
}



