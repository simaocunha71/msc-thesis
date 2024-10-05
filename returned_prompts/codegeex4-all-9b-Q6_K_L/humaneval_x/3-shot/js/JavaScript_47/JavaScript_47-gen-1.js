  let sorted_l = l.sort((a, b) => a - b);
  let mid = Math.floor(sorted_l.length / 2);
  return sorted_l.length % 2 === 0 ? (sorted_l[mid - 1] + sorted_l[mid]) / 2 : sorted_l[mid];
}

