  let len = l.length;
  let sorted = l.slice().sort((a, b) => a - b);
  if (len % 2 !== 0) {
    return sorted[Math.floor(len / 2)];
  } else {
    let mid = len / 2;
    let left = sorted[mid - 1];
    let right = sorted[mid];
    return (left + right) / 2;
  }
}



