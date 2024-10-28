  let [_, apples, oranges] = s.match(/^(\d+)\s*apple(s?)\s*and\s*(\d+)\s*orange(s?)$/);
  apples = parseInt(apples);
  oranges = parseInt(oranges);
  return n - apples - oranges;
}