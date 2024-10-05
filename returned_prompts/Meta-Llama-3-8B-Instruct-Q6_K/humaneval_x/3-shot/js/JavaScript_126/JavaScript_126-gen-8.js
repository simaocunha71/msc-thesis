  for (let i = 1; i < lst.length; i++) {
    if (lst[i] <= lst[i - 1]) {
      return false;
    }
  }
  return lst.every((x, i, a) => x === a[0]);
} // Note: This code doesn't handle the case where the list is empty. For a complete solution, add a check for that case at the beginning of the function: return lst.length === 0; // The list is empty, so it is sorted.