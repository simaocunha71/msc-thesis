  let [apples, oranges] = [...s.matchAll(/(\d+) (apples|oranges)/g)].map(m => parseInt(m[1]));
  return n - apples - oranges;
}



