  let evenCount = 0;

  for (let num of lst1) {
    if (num % 2 === 0) {
      evenCount++;
    }
  }

  if (evenCount === lst1.length) {
    return "YES";
  }

  for (let num of lst2) {
    if (num % 2 === 0) {
      evenCount++;
    }
  }

  if (evenCount === lst1.length) {
    return "YES";
  }

  return "NO";
}  // Time Complexity: O(n), where n is the total number of elements in both lists. Space Complexity: O(1) as we are not using any extra space.