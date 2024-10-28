  let [apples, oranges] = s.match(/(\d+) (apples|oranges)/g).map(x => parseInt(x.match(/\d+/)[0]));
  return n - apples - oranges;
}*/



