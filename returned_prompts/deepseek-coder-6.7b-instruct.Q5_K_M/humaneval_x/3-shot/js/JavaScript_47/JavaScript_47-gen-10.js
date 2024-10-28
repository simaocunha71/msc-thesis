  l.sort((a, b) => a - b);
  let mid = Math.floor(l.length / 2);

  return l.length % 2 !== 0 ? l[mid] : (l[mid - 1] + l[mid]) / 2;
}



