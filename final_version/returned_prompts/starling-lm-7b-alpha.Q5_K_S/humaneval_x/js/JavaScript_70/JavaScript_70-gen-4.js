  let sorted = [...lst];
  let remaining = [...lst];
  let i = 0;
  while (sorted.length < lst.length) {
    sorted[i] = Math.min(...remaining);
    remaining.splice(remaining.indexOf(sorted[i]), 1);
    i += 1;
  }

  return sorted;
}



