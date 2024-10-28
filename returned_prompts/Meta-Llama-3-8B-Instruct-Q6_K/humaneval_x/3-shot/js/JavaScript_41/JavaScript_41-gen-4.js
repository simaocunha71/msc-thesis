  let collisions = 0;
  let positions = [];
  for (let i = 0; i < n; i++) {
    positions.push(i);
  }
  for (let i = 0; i < n; i++) {
    positions.push(n - i);
  }
  positions.sort((a, b) => a - b);
  for (let i = 0; i < positions.length - 1; i++) {
    if (Math.abs(positions[i] - positions[i + 1]) < 1) {
      collisions++;
    }
  }
  return collisions;
}
//Time complexity: O(nlogn) because of the sort operation. Space complexity: O(n) for the positions array.