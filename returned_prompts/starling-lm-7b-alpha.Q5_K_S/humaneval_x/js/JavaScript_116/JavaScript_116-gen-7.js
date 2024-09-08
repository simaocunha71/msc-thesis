  const binary_counts = arr.map(n => {
    const s = n.toString(2);
    return { value: n, count: s.length, binary: s };
  });

  return binary_counts.sort((a, b) => {
    if (a.count < b.count) {
      return -1;
    } else if (a.count > b.count) {
      return 1;
    } else {
      return a.value - b.value;
    }
  }).map(n => n.value);
}



