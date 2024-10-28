  l.sort((a, b) => a - b);

  let middle = Math.floor(l.length / 2);

  if (l.length % 2)
    return l[middle];
  else
    return (l[middle - 1] + l[middle]) / 2.0;
}



