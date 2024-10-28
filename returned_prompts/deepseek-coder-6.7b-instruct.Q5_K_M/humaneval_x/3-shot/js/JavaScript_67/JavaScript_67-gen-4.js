  let [apples, oranges] = [...s.matchAll(/(\d+) apples/g), ...s.matchAll(/(\d+) oranges/g)].map(m => parseInt(m[1]));
  return n - apples - oranges;
}



