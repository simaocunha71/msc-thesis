  l.sort((a, b) => a - b);
  let length = l.length;
  if (length % 2 == 1) {
    return l[length / 2];
  } else {
    return (l[length / 2] + l[(length / 2) - 1]) / 2;
  }
}



