  let [apple, oranges] = s.match(/\d+/g).map(Number);
  return n - apple - oranges;
}



