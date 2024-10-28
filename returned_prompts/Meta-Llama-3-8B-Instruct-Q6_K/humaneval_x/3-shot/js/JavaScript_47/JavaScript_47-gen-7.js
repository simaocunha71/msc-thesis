  l.sort((a, b) => a - b);
  let half = Math.floor(l.length / 2);
  if (l.length % 2 === 0) {
    return (l[half - 1] + l[half]) / 2;
  } else {
    return l[half];
  }
}  // O(n log n) time complexity due to sorting. Can be optimized to O(n) if the input array is already sorted.  // O(1) space complexity.