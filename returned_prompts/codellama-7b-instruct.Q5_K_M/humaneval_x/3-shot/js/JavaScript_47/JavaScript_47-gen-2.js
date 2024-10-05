  l.sort();
  const mid = Math.floor(l.length / 2);
  if (l.length % 2 == 0) {
    return (l[mid] + l[mid - 1]) / 2.0;
  } else {
    return l[mid];
  }
}



