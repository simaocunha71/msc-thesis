  let sorted_l = l.slice().sort((a, b) => a - b);
  let length = sorted_l.length;
  if (length % 2 == 0) {
    return (sorted_l[length / 2 - 1] + sorted_l[length / 2]) / 2.0;
  } else {
    return sorted_l[Math.floor(length / 2)];
  }
}



