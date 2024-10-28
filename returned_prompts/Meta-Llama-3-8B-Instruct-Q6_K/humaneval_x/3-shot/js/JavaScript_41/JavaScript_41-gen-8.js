  let collisions = 0;
  for (let i = 1; i <= n; i++) {
    for (let j = 1; j <= n; j++) {
      if (i !== j) {
        let distance = Math.abs(i - j);
        if (distance % 1 === 0) {
          collisions += 1;
        }
      }
    }
  }
  return collisions;
} // O(n^2) time complexity, not very efficient for large values of n.  If you need a more efficient solution, consider using a different data structure like a hash set.  For example, you could create a set of all possible distances, and then count the number of collisions by checking if a distance is in the set.  This would reduce the time complexity to O(n).  However, this would require more space to store the set.  Depending on the constraints of your problem, one approach may be more suitable than the other. 