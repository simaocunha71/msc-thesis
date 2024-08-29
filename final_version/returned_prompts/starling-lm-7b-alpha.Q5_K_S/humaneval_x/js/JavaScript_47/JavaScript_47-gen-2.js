  l.sort((a, b) => a - b);
  let length = l.length;
  if (length % 2 === 0) {
    let mid = length / 2;
    return (l[mid - 1] + l[mid]) / 2;
  } else {
    return l[Math.floor(length / 2)];
  }
}



