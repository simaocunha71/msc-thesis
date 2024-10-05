  let [apples，oranges] = s.match(/\d+/g) .map(Number);
  return n - apples - oranges - 0;
}
console.