  l.sort();
  if (l.length % 2 == 0) {
    return (l[l.length / 2] + l[l.length / 2 - 1]) / 2;
  } else {
    return l[Math.floor(l.length / 2)];
  }
}



