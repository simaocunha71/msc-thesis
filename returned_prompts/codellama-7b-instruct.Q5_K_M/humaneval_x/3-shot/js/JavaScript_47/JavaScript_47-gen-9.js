  l.sort();
  if (len % 2 == 0) {
    return (l[l.length / 2 - 1] + l[l.length / 2]) / 2.0;
  } else {
    return l[l.length / 2];
  }
}



