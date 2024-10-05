  let [apples, oranges] = s.match(/(\d+)\s*apple(s?)\s*and\s*(\d+)\s*orange(s?)/).slice(1).map(Number);
  return n - apples - oranges;
}